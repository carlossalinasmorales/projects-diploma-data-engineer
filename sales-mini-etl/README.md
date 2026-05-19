# Sales Mini ETL

![Python](https://img.shields.io/badge/Python-3.12+-3776AB?style=for-the-badge&logo=python&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-0.115-009688?style=for-the-badge&logo=fastapi&logoColor=white)
![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-2.0-D71F00?style=for-the-badge&logo=sqlalchemy&logoColor=white)
![SQLite](https://img.shields.io/badge/SQLite-Database-003B57?style=for-the-badge&logo=sqlite&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-2.2-150458?style=for-the-badge&logo=pandas&logoColor=white)
![Pydantic](https://img.shields.io/badge/Pydantic-2.9-E92063?style=for-the-badge&logo=pydantic&logoColor=white)
![Uvicorn](https://img.shields.io/badge/Uvicorn-ASGI-4051B5?style=for-the-badge)
![uv](https://img.shields.io/badge/uv-Package%20Manager-DE5FE9?style=for-the-badge)

## Requisitos

- Python 3.12+
- `uv` instalado

Si no tienes `uv`:

```bash
pip install uv
```

## Revisión rápida

Si alguien solo quiere levantar y revisar el proyecto, estos son los pasos mínimos.

### 1. Instalar dependencias con `uv`

```bash
uv sync
```

### 2. Ejecutar el scheduler

```bash
uv run python scheduler.py
```

### 3. Ejecutar el ETL directo con fallo provocado

```bash
uv run python etl.py --fallo
```

Eso genera evidencia en:
- `logs/etl.log`
- `logs/alertas.log`

### 4. Levantar la API con Uvicorn

```bash
uv run uvicorn main:app --reload
```

### 5. Revisar endpoints desde Swagger Docs

Abrir en el navegador:

```text
http://127.0.0.1:8000/docs
```

Ahí se pueden probar:
- `GET /`
- `GET /resumen`
- `GET /top-productos?n=5`


## Estructura del proyecto

```text
sales-mini-etl/
├── data/
│   └── ventas_marzo.csv
├── db/
│   └── ventas.db
├── logs/
│   ├── etl.log
│   └── alertas.log
├── database.py
├── etl.py
├── main.py
├── models.py
├── scheduler.py
├── schemas.py
├── pyproject.toml
└── README.md
```

## Qué hace cada archivo

| Archivo | Función |
|---|---|
| `etl.py` | Ejecuta extract, transform y load |
| `scheduler.py` | Corre el ETL automáticamente por ciclos |
| `main.py` | Expone la API con FastAPI |
| `database.py` | Configura la conexión SQLAlchemy |
| `models.py` | Modelos ORM de SQLAlchemy |
| `schemas.py` | Schemas Pydantic de respuesta |
| `data/ventas_marzo.csv` | Fuente de datos |
| `db/ventas.db` | Base SQLite |
| `logs/etl.log` | Logs JSON del ETL |
| `logs/alertas.log` | Alertas cuando falla una etapa |

## Notas
- `scheduler.py` cuenta con variables para acelerar `segundos_de_ejecucion` y `ciclos` para acelerar la revisión.
- La API y el scheduler se ejecutan por separado.
- Primero conviene correr el ETL al menos una vez para tener datos en SQLite.
- Si `/resumen` no devuelve datos, probablemente todavía no corriste el ETL.
