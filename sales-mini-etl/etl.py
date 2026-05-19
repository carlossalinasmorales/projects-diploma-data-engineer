from __future__ import annotations
import sqlite3
import uuid
from datetime import datetime, timezone
from pathlib import Path
import pandas as pd

BASE_DIR = Path(__file__).resolve().parent
CSV_PATH = BASE_DIR / "data" / "ventas_marzo.csv"
DB_PATH = BASE_DIR / "db" / "ventas.db"

#Funcion para extraer datos de ventas desde un CSV
def extract_sales(csv_path):
    return pd.read_csv(csv_path)


#Funcion para transformar datos de ventas segun requerimientos
def transform_sales(sales, run_id):
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

    return resumen, top_productos, timestamp


#Funcion para cargar tablas en SQLite
def load_sales(resumen, top_productos, db_path):
    with sqlite3.connect(db_path) as connection:
        resumen.to_sql("resumen", connection, if_exists="append", index=False)
        top_productos.to_sql("top_productos", connection, if_exists="replace", index=False)


# Funcion para correr el ETL completo
def run_etl(csv_path, db_path):
    run_id = uuid.uuid4().hex[:8]
    timestamp = datetime.now(timezone.utc).isoformat(timespec="seconds")
    sales = extract_sales(csv_path)
    resumen, top_productos, timestamp = transform_sales(sales, run_id)
    load_sales(resumen, top_productos, db_path)
    return run_id, timestamp


# # Configuracion para ejecutar script (no necesaria ya que se ejecuta en scheduler.py)
# if __name__ == "__main__":
#     generated_run_id, generated_timestamp = run_etl(CSV_PATH, DB_PATH)
#     print(f"ETL Completado exitosamente. run_id={generated_run_id}, timestamp={generated_timestamp}")
