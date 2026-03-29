#!/usr/bin/env bash

set -euo pipefail # Detiene el pipeline si algo falla

#Aqui se establece las carpeta raiz para mejorar la automatizacion del script
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_ROOT="$(cd "$SCRIPT_DIR/.." && pwd)"

CSV_FILE_NAME="titanic.csv"
OUTPUT_FILE_NAME="class_count.txt"
ERROR_FILE_NAME=error.log

#Carpetas de archivos especificos
DATA_DIR="$PROJECT_ROOT/data/raw"
OUTPUT_DIR="$PROJECT_ROOT/output"
LOG_DIR="$PROJECT_ROOT/logs"

#Archivos especificos
CSV_FILE="$DATA_DIR/$CSV_FILE_NAME"
OUTPUT_FILE="$OUTPUT_DIR/$OUTPUT_FILE_NAME"
ERROR_LOG="$LOG_DIR/$ERROR_FILE_NAME"

#TOKEN
TOKEN_CURSO="FAE_Usach"

echo VARIABLES DE DIRECTORIOS CREADAS CORRECTAMENTE


if wget -O "$CSV_FILE" https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv 2> "$ERROR_LOG"; then
  echo "[OK] $CSV_FILE_NAME CREADO CORRECTAMENTE"
else
  echo "[ERROR] Algo fallo, al crear $CSV_FILE_NAME revisar $ERROR_FILE_NAME"
fi

if echo "Reporte generado por: $USER el $(date) - Token: $TOKEN_CURSO" > "$OUTPUT_FILE"; then
  echo "[OK] REPORT USER Y TOKEN CREADO CORRECTAMENTE"
else
  echo "[ERROR] ALGO FALLO AL CREAR REPORT USER Y TOKEN EN $OUTPUT_FILE_NAME"
fi

if tail -n +2 "$CSV_FILE" | cut -d',' -f3 | sort | uniq -c | sort -nr >> "$OUTPUT_FILE"; then
  echo "[OK] $CSV_FILE_NAME TRANSFORMADO CORRECTAMENTE"
else
  echo "[ERROR] PROBLEMAS AL TRANSFORMAR $CSV_FILE_NAME"
fi

echo "******* OUTPUT GENERADO *******"
if cat $OUTPUT_FILE; then
  echo "******************************"
  echo "[OK] PIPELINE EJECUTADO CON EXITO"
else
  echo "[ERROR] FALLA AL LEER OUTPUT CREADO"
fi

exit 0
