# 02 · Data Algorithms

![Python](https://img.shields.io/badge/Python-3.12+-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Jupyter](https://img.shields.io/badge/Notebook-Algorithm%20Practice-F37626?style=for-the-badge&logo=jupyter&logoColor=white)

Módulo de práctica para análisis de algoritmos y estructuras de datos usando notebooks en Python.

## Executive Summary

Este track documenta ejercicios introductorios para razonar sobre tiempos de ejecución, estructuras de datos, hashing y grafos en formato notebook.

Actualmente incluye:

- `01-analisis-algoritmo.ipynb`
- `02-edd-lineales.ipynb`
- `02-actividad-edd-lineales.ipynb`
- `03-arboles.ipynb`
- `04-hashing.ipynb`
- `04-actividad-hashing.ipynb`
- `05-grafos.ipynb`
- `05-actividad-grafos.ipynb`

## Tech Stack

`Python 3.12+` · `Jupyter Notebook` · `uv` · `ipykernel`

## Project Structure

```text
.
├── 01-analisis-algoritmo.ipynb
├── 02-edd-lineales.ipynb
├── 02-actividad-edd-lineales.ipynb
├── 03-arboles.ipynb
├── 04-hashing.ipynb
├── 04-actividad-hashing.ipynb
├── 05-grafos.ipynb
├── 05-actividad-grafos.ipynb
├── data/
│   ├── output/
│   │   └── .gitkeep
│   └── raw/
│       └── .gitkeep
├── pyproject.toml
├── uv.lock
├── .gitignore
└── README.md
```

## Quick Start

Desde este directorio:

```bash
uv sync
```

Luego abrí el notebook que quieras trabajar con tu entorno preferido (por ejemplo, VS Code o Jupyter).

## Why this project matters

El análisis algorítmico es parte del criterio técnico: ayuda a decidir soluciones más eficientes antes de escalar procesamiento de datos y modelar estructuras correctas para cada problema.

## Notes

- Este módulo prioriza práctica conceptual con notebooks progresivos por tema.
- Los directorios `data/raw/` y `data/output/` se preservan con `.gitkeep`, pero su contenido de trabajo queda fuera del repo.
- La dependencia declarada actualmente es `ipykernel`.
