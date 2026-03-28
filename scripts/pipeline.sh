#!/usr/bin/env bash

set -euo pipefail # Detiene el pipeline si algo falla

#Aqui se establece las carpeta raiz para mejorar la automatizacion del script
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_ROOT="$(cd "$SCRIPT_DIR/.." && pwd)"

#Carpetas de archivos especificos
DATA_DIR="$PROJECT_ROOT/data/raw"
OUTPUT_DIR="$PROJECT_ROOT/output"
LOG_DIR="$PROJECT_ROOT/logs"

#Archivos especificos
CSV_FILE="$DATA_DIR/titanic.csv"
REPORT_FILE="$OUTPUT_DIR/class_count.txt"
ERROR_LOG="$LOG_DIR/error.log"

#TOKEN
TOKEN_CURSO="FAE_Usach"

echo VARIABLES DE DIRECTORIOS CREADAS CORRECTAMENTE


if wget -O "$CSV_FILE" https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv 2> "$ERROR_LOG"; then
  echo "[OK] $CSV_FILE CREADO CORRECTAMENTE"
else
  echo "[ERROR] Algo fallo, revisar $ERROR_LOG"
fi

if echo "Reporte generado por: $USER el $(date) - Token: $TOKEN_CURSO" > "$REPORT_FILE"; then
  echo "[OK] REPORT USER Y TOKEN CREADO CORRECTAMENTE"
else
  echo "[ERROR] Algo fallo, revisar creacion de inea de reporte"
fi

if tail -n +2 "$CSV_FILE" | cut -d',' -f3 | sort | uniq -c | sort -nr >> "$REPORT_FILE"; then
  echo "[OK] $CSV_FILE TRANSFORMADO CORRECTAMENTE"
else
  echo "[ERROR] PROBLEMAS AL TRANSFORMAR $CSV_FILE"
fi

echo "[OK END]"
