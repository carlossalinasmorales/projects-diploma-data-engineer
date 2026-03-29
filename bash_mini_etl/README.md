# Mini Bash ETL

Pipeline ETL básico escrito en Bash que procesa el dataset Titanic del repositorio de DataScienceDojo.

## Descripción

Este proyecto implementa un pipeline ETL simple que:
1. **Extract**: Descarga el archivo CSV de Titanic desde GitHub
2. **Transform**: Cuenta pasajeros por clase (columna 3 del CSV)
3. **Load**: Guarda los resultados en archivos de salida y logs

## Estructura del Proyecto

```
bash_mini_etl/
├── data/raw/          # Datos crudos descargados
├── logs/              # Logs de errores
├── output/            # Resultados del pipeline
├── scripts/
│   └── pipeline.sh    # Script principal del ETL
├── .gitignore
├── SDD.md             # Especificación de diseño
└── README.md
```

## Requisitos

- Bash 4.0+
- `wget` para descarga de archivos

## Uso

Ejecutar desde la raíz del proyecto:

```bash
cd bash_mini_etl
cd scripts
./pipeline.sh
```

## Salida

- **output/class_count.txt**: Reporte con conteo de pasajeros por clase
- **logs/error.log**: Registro de errores durante la ejecución
