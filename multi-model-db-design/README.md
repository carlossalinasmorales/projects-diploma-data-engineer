# Base de Datos Multimodelo — Gestión de Mantenciones

Proyecto académico del módulo **Modelos y Gestión de Bases de Datos** del Diplomado en Data Engineer.

## Descripción

Este proyecto desarrolla un caso de **base de datos multimodelo** aplicado a la gestión de mantenciones técnicas de unidades de climatización/refrigeración industrial instaladas en sucursales de empresas cliente.

El trabajo distribuye el modelo conceptual en cuatro paradigmas de bases de datos:

- [Versión Markdown del informe](bbdd-multimodel-gestion-mantenciones.md)

- **Relacional (SQL):** empresa, sucursal, equipo y ticket.
- **Columnar (Cassandra):** sensores, lecturas y alertas.
- **Documental (MongoDB):** informes técnicos, actividades y evidencias.
- **Grafos (Neo4j):** técnicos, especialidades y zonas de cobertura.

## Contenido del informe

El informe incluye:

1. modelo conceptual mediante diagrama de clases UML;
2. justificación de la distribución por paradigma;
3. transformación conceptual a modelo relacional;
4. consultas SQL con posibles resultados;
5. modelo columnar en Cassandra y consultas CQL;
6. documentos JSON para MongoDB y consultas MQL;
7. grafo en Neo4j y consultas Cypher;
8. cierre de coherencia técnica.

## Objetivo académico

Diseñar, transformar e implementar un modelo de datos multimodelo a partir de un problema real, justificando las decisiones de modelado según la semántica de los datos y los patrones de consulta.
