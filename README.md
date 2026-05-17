# Diploma Data Engineer

![Python](https://img.shields.io/badge/Python-3.12+-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-Data%20Analysis-150458?style=for-the-badge&logo=pandas&logoColor=white)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-SQL-4169E1?style=for-the-badge&logo=postgresql&logoColor=white)
![Jupyter](https://img.shields.io/badge/Jupyter-Notebooks-F37626?style=for-the-badge&logo=jupyter&logoColor=white)
![Bash](https://img.shields.io/badge/Bash-ETL-121011?style=for-the-badge&logo=gnubash&logoColor=white)

Portafolio técnico con proyectos prácticos de **Data Engineering** desarrollados durante el diplomado de la **Universidad de Santiago de Chile (USACH)**.

Está orientado a demostrar base sólida en:

- **ETL y automatización con Bash**
- **análisis de datos con Python y pandas**
- **trabajo con notebooks en Jupyter**
- **consultas SQL sobre PostgreSQL**

## Executive Summary

Este monorepo concentra ejercicios reales y académicos que muestran capacidad para trabajar con datos desde distintas capas del flujo:

- ingesta y procesamiento básico,
- exploración y transformación,
- análisis tabular,
- consultas relacionales.

La idea NO es mostrar solo notebooks sueltos, sino evidencia de criterio técnico, separación por módulos y documentación por proyecto.

## Tech Stack :o

`Python` · `pandas` · `Jupyter` · `SQL` · `PostgreSQL` · `Bash` · `uv` · `wget`

## Projects

| Proyecto | Enfoque | Stack | Link |
| --- | --- | --- | --- |
| `bash-mini-etl` | Pipeline ETL básico sobre Titanic con extracción, transformación y salida procesada. | Bash, `wget` | [README](bash-mini-etl/README.md) |
| `jupyter-playground` | Playground de notebooks para preprocesamiento y ejercicios de datos. | Python, Jupyter, `uv` | [README](jupyter-playground/README.md) |
| `pandas-sales-analysis` | Análisis de ventas desde CSV con generación de resumen procesado. | Python, pandas, Jupyter | [README](pandas-sales-analysis/README.md) |
| `postgres-basic-queries` | Práctica de consultas SQL sobre `dvdrental`. | PostgreSQL, SQL | [README](postgres-basic-queries/README.md) |
| `multi-model-db-design` | Practica de Modelado Multimodelo | UML, SQL, MongoDB, Cassandra, Neo4j  | [README](multi-model-db-design/README.md) |

## Repository Structure

```text
.
├── bash-mini-etl/
├── jupyter-playground/
├── pandas-sales-analysis/
├── postgres-basic-queries/
└── README.md
```

## Why this repository matters

Este portfolio refleja habilidades aplicadas en problemas comunes de ingeniería y análisis de datos:

- estructurar proyectos por dominio,
- documentar flujos de trabajo,
- procesar datasets con herramientas distintas según el caso,
- combinar scripting, análisis y SQL en un mismo repositorio.

## Quick Start

```bash
git clone <repo-url>
cd diploma-data-engineer
```

Después, elige el módulo que quieras revisar y seguí su README específico:

- [bash-mini-etl](bash-mini-etl/README.md)
- [jupyter-playground](jupyter-playground/README.md)
- [pandas-sales-analysis](pandas-sales-analysis/README.md)
- [postgres-basic-queries](postgres-basic-queries/README.md)
- [multi-model-db-design](multi-model-db-design/README.md)

## Requirements

- **Python 3.12+**
- **Jupyter Notebook / JupyterLab**
- **uv**
- **Bash 4+**
- **wget**
- **PostgreSQL** con base de ejemplo `dvdrental`

## Notes

- Cada subproyecto tiene contexto, instalación y alcance propio.
- El repositorio sigue creciendo a medida que avanza el diplomado.
- Algunos módulos están más maduros que otros, lo cual refleja el progreso real del aprendizaje.
