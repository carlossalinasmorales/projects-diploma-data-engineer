# Distributed Systems

[![Python 3.12](https://img.shields.io/badge/Python-3.12-blue)](./pyproject.toml)
[![PySpark 4.1.2](https://img.shields.io/badge/PySpark-4.1.2-E25A1C)](./pyproject.toml)
[![Pandas 3.0.3](https://img.shields.io/badge/Pandas-3.0.3-150458)](./pyproject.toml)
[![Jupyter Notebooks](https://img.shields.io/badge/Formato-Jupyter_Notebooks-F37626)](./01-pyspark-practice.ipynb)
[![uv lock](https://img.shields.io/badge/Entorno-uv_lock-5C4EE5)](./uv.lock)

Proyecto práctico orientado a explorar procesamiento distribuido con PySpark desde notebooks. La carpeta contiene dos recorridos complementarios: uno de fundamentos con datos sintéticos de práctica y otro de transformaciones avanzadas sobre CSV, JSON y Parquet.

## Visión general

Este proyecto funciona como playground de aprendizaje para trabajar conceptos clave de Spark SQL y DataFrames en modo local:

- lectura de fuentes CSV, JSON Lines, JSON con `multiLine` y Parquet
- definición explícita de esquemas
- limpieza y filtrado de datos
- transformaciones con columnas, fechas, strings y arrays
- agregaciones, joins y persistencia en CSV/Parquet
- SQL sobre vistas temporales, UDFs, window functions y escritura particionada

El contenido está centrado en notebooks y archivos de datos ya generados, no en una aplicación empaquetada ni en pipelines productivos.

## Estructura del proyecto

```text
distributed-systems/
├── 01-pyspark-practice.ipynb
├── 02-pyspark-advanced-transformation.ipynb
├── 01-data/
├── 02-data/
├── pyproject.toml
├── uv.lock
└── .python-version
```

## Notebooks

### `01-pyspark-practice.ipynb`

Notebook de fundamentos de PySpark con foco en práctica guiada sobre un mini dominio comercial.

Incluye:

- creación de `SparkSession` local
- generación de datasets sintéticos con Pandas
- lectura de datasets tabulares generados dentro de `01-data/`
- inspección de esquema, conteos y estadísticas básicas
- selección, filtros, columnas derivadas y lógica condicional
- trabajo con fechas y clasificación de ventas
- agregaciones por sucursal, categoría y segmento
- joins entre ventas, productos y clientes
- escritura de resultados dentro de `01-data/` como CSV, Parquet y CSV único con `coalesce(1)`

### `02-pyspark-advanced-transformation.ipynb`

Notebook de transformaciones avanzadas y formatos de almacenamiento en Spark.

Incluye:

- lectura correcta de un CSV problemático con delimitador `;`, comillas y `dateFormat`
- lectura de JSON Lines y JSON con `multiLine`
- acceso a structs, arrays y uso de `explode`
- comparación práctica entre CSV y Parquet
- trabajo con datasets de práctica almacenados dentro de `02-data/`
- limpieza de viajes, métricas horarias y análisis por método de pago
- uso de Spark SQL, UDFs y window functions
- escritura particionada y generación de salidas dentro de `02-data/`

## Stack

- Python `>=3.12`
- PySpark `>=4.1.2`
- Pandas `>=3.0.3`
- Jupyter / IPython kernel (`ipykernel`)
- `uv` como gestor de entorno y lockfile

## Puesta en marcha

El proyecto tiene `pyproject.toml`, `uv.lock` y `.python-version`, así que la forma más consistente de levantarlo es con `uv`.

### 1. Crear o sincronizar el entorno

```bash
uv sync
```

### 2. Registrar el kernel de Jupyter

```bash
uv run python -m ipykernel install --user --name distributed-systems
```

### 3. Abrir los notebooks

```bash
uv run jupyter lab
```

Si prefieres Jupyter Notebook clásico:

```bash
uv run jupyter notebook
```

## Cómo recorrer el proyecto

Orden sugerido:

1. `01-pyspark-practice.ipynb` para repasar DataFrames, filtros, joins y escrituras básicas.
2. `02-pyspark-advanced-transformation.ipynb` para formatos, optimización conceptual, SQL, UDFs, ventanas y particionado.

## Datos y salidas

### Carpetas de datos

- `01-data/`: aquí se crean y reutilizan los datos del notebook introductorio a medida que ejecutas el flujo.
- `02-data/`: aquí se crean y reutilizan los datos, temporales y salidas del notebook avanzado a medida que ejecutas el flujo.

### Nota sobre versionado de datos

`.gitignore` excluye `01-data/*`, `02-data/*` y `.venv`, así que estas carpetas están pensadas para ir generando datos y resultados locales según ejecutes los notebooks, no como fuente estable versionada.

## Qué aporta este proyecto

- muestra una progresión clara desde PySpark básico hasta transformaciones más cercanas a casos reales
- deja ejemplos concretos de lectura, tipado, limpieza, joins y escrituras en varios formatos
- sirve como material de estudio para comparar decisiones comunes en Spark, como CSV vs Parquet o escritura normal vs particionada
- deja artefactos y resultados que ayudan a entender cómo Spark materializa salidas en disco

## Valor de aprendizaje

Si abres esta carpeta por separado, el valor principal está en ver PySpark en contexto práctico, con datasets pequeños para aprender y un dataset más grande para observar patrones reales de procesamiento y salida.
