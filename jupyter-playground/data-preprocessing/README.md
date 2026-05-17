# 01 · Data Preprocessing

![Python](https://img.shields.io/badge/Python-3.12-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Pandas](https://img.shields.io/badge/pandas-2.2.3-150458?style=for-the-badge&logo=pandas&logoColor=white)
![Jupyter](https://img.shields.io/badge/JupyterLab-4.4+-F37626?style=for-the-badge&logo=jupyter&logoColor=white)

Track práctico de preprocesamiento con notebooks para consolidar fundamentos de Python y análisis de datos.

## Executive Summary

Este módulo reúne ejercicios progresivos para trabajar capacidades clave de entrada en Data Engineering:

- estructuras y control de flujo en Python,
- manipulación tabular con `pandas`,
- exploración inicial de datos (EDA),
- lectura/escritura de archivos en escenarios de laboratorio.

El foco está en base técnica reproducible y ordenada, no en demos aisladas.

## Tech Stack

`Python 3.12` · `pandas` · `NumPy` · `JupyterLab` · `uv` · `ruff` · `pip-audit`

## Quick Start

Desde este directorio:

```bash
uv sync --dev
uv run jupyter lab
```

Si trabajás en VS Code, también podés abrir directamente los `.ipynb` usando el kernel del `.venv`.

## Notebook Map

- `01-introduccion.ipynb`
- `02-estructuras-de-datos.ipynb`
- `03-estructuras-de-control.ipynb`
- `04-funciones.ipynb`
- `05-pandas.ipynb` y `05-pandas-ejercicio.ipynb`
- `06-eda.ipynb`
- `07-archivos.ipynb`
- `08-numpy.ipynb` y `08-numpy_imagen.ipynb`
- `09-api.ipynb`

## Environment Conventions

- Entorno virtual local en `.venv/`.
- Dependencias declaradas en `pyproject.toml` y congeladas en `uv.lock`.
- Versión de Python acotada por `.python-version` y `requires-python`.
- VS Code configurado para usar `${workspaceFolder}/.venv/bin/python`.

## Quality Commands

```bash
uv run ruff check .
uv run ruff check . --fix
uv run pip-audit --local
```

## Why this project matters

Antes de diseñar pipelines complejos, hay que dominar limpieza y comprensión de datos. Este track evidencia ese cimiento técnico.

## Notes

- La fuente de verdad del entorno es `pyproject.toml` + `uv.lock`.
- `requirements.txt` no forma parte del flujo recomendado en este módulo.
