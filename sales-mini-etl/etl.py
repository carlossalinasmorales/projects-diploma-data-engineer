from __future__ import annotations
import sys
import sqlite3
import time
import uuid
from datetime import datetime, timezone
from pathlib import Path
import pandas as pd
import logging
from pythonjsonlogger import jsonlogger

#Configuracion de rutas
BASE_DIR = Path(__file__).resolve().parent
CSV_PATH = BASE_DIR / "data" / "ventas_marzo.csv"
DB_PATH = BASE_DIR / "db" / "ventas.db"
LOG_PATH = BASE_DIR / "logs" / "etl.log"
ALERTS_PATH = BASE_DIR / "logs" / "alertas.log"
# LOG_PATH.parent.mkdir(parents=True, exist_ok=True)

#---------------------------------------Logger Config-------------------------------------------

#Configuracion del logger
logger = logging.getLogger("etl")
logger.setLevel(logging.INFO)
if not logger.handlers:
    handler = logging.FileHandler(LOG_PATH, encoding="utf-8")
    formatter = jsonlogger.JsonFormatter(
        "%(timestamp)s %(levelname)s %(message)s %(run_id)s %(etapa)s %(duracion_ms)s %(status)s",
        rename_fields={"levelname": "level"}
    )
    handler.setFormatter(formatter)
    logger.addHandler(handler)

#Logs estructurados para cada etapa del proceso ETL
def log_event(level, message, run_id, etapa, status, duracion_ms=None):
    extra_data = {
        "timestamp": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        "run_id": run_id,
        "etapa": etapa,
        "status": status,
        "duracion_ms": duracion_ms,
    }
    if level == "INFO":
        logger.info(message, extra=extra_data)
    elif level == "ERROR":
        logger.error(message, extra=extra_data)
    elif level == "WARNING":
        logger.warning(message, extra=extra_data)

#Funcion para escribir alertas en un archivo de texto
def write_alert(run_id, etapa, error):
    timestamp = datetime.now(timezone.utc).isoformat(timespec="seconds")
    with open(ALERTS_PATH, "a", encoding="utf-8") as file:
        file.write(
            f"[ALERTA] run_id={run_id} etapa={etapa} timestamp={timestamp} error={error}\n"
        )

#----------------------------------- ETL -----------------------------------------------

#Funcion para extraer datos de ventas desde un CSV
def extract_sales(csv_path, run_id, fallo=False):
    log_event("INFO", "etapa_inicio", run_id, "extract", "OK")
    start = time.perf_counter()
    try:
        if fallo:
            write_alert(run_id, "extract", "Fallo provocado para testing")
            print(f"Fallo provocado para testing, revisa la alerta en logs/alertas.log. run_id={run_id}")
        sales = pd.read_csv(csv_path)
        duracion_ms = round((time.perf_counter() - start) * 1000, 2)
        log_event("INFO", "etapa_fin", run_id, "extract", "OK", duracion_ms)
        return sales
    except Exception as error:
        duracion_ms = round((time.perf_counter() - start) * 1000, 2)
        log_event("ERROR", "etapa_error", run_id, "extract", "ERROR", duracion_ms)
        write_alert(run_id, "extract", str(error))
        raise

#Funcion para transformar datos de ventas segun requerimientos
def transform_sales(sales, run_id):
    log_event("INFO", "etapa_inicio", run_id, "transform", "OK")
    start = time.perf_counter()
    try:
        total_ventas = int(sales["total"].sum())
        n_transacciones = int(len(sales))
        ticket_promedio = int(total_ventas / n_transacciones)
        clientes_unicos = int(sales["cliente_id"].nunique())

        timestamp = datetime.now(timezone.utc).isoformat(timespec="seconds")

        resumen = pd.DataFrame(
            [
                {
                    "run_id": run_id,
                    "timestamp": timestamp,
                    "total_ventas": total_ventas,
                    "n_transacciones": n_transacciones,
                    "ticket_promedio": ticket_promedio,
                    "clientes_unicos": clientes_unicos,
                }
            ]
        )

        top_productos = (
            sales.groupby(["sku", "producto"], as_index=False)
            .agg(total_vendido=("total", "sum"))
            .rename(columns={"producto": "nombre"})
            .sort_values("total_vendido", ascending=False)
        )
        duracion_ms = round((time.perf_counter() - start) * 1000, 2)
        log_event("INFO", "etapa_fin", run_id, "transform", "OK", duracion_ms)
        return resumen, top_productos, timestamp

    except Exception as error:
        duracion_ms = round((time.perf_counter() - start) * 1000, 2)
        log_event("ERROR", "etapa_error", run_id, "transform", "ERROR", duracion_ms)
        write_alert(run_id, "transform", str(error))
        raise


#Funcion para cargar tablas en SQLite
def load_sales(resumen, top_productos, db_path, run_id):
    log_event("INFO", "etapa_inicio", run_id, "load", "OK")
    start = time.perf_counter()
    try:
        with sqlite3.connect(db_path) as connection:
            resumen.to_sql("resumen", connection, if_exists="append", index=False)
            top_productos.to_sql("top_productos", connection, if_exists="replace", index=False)

        duracion_ms = round((time.perf_counter() - start) * 1000, 2)
        log_event("INFO", "etapa_fin", run_id, "load", "OK", duracion_ms)
    except Exception as error:
        duracion_ms = round((time.perf_counter() - start) * 1000, 2)
        log_event("ERROR", "etapa_error", run_id, "load", "ERROR", duracion_ms)
        write_alert(run_id, "load", str(error))
        raise


# Orquestador del proceso ETL
def run_etl_orquestator(csv_path, db_path, fallo=False):
    run_id = uuid.uuid4().hex[:8]
    start = time.perf_counter()

    log_event("INFO", "etapa_inicio", run_id, "run", "OK")
    print(f"Iniciando ETL.")
    try:
        sales = extract_sales(csv_path, run_id, fallo)
        resumen, top_productos, timestamp = transform_sales(sales, run_id)
        load_sales(resumen, top_productos, db_path, run_id)

        duracion_ms = round((time.perf_counter() - start) * 1000, 2)
        log_event("INFO", "etapa_fin", run_id, "run", "OK", duracion_ms)
        print(f"ETL completado. run_id={run_id}, timestamp={timestamp}")
        return run_id, timestamp
    except Exception as error:
        duracion_ms = round((time.perf_counter() - start) * 1000, 2)
        log_event("ERROR", "etapa_error", run_id, "run", "ERROR", duracion_ms)
        write_alert(run_id, "run", str(error))
        print(f"ERROR en ETL. run_id={run_id}, timestamp={timestamp}")
        raise


#Configuracion para correr directamente etl.py sin scheduler (utilizas --fallo para testear alerta.log)
if __name__ == "__main__":
    fallo = "--fallo" in sys.argv
    run_id, timestamp = run_etl_orquestator(CSV_PATH, DB_PATH, fallo)
    
