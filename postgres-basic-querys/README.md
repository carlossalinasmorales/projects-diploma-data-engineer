# Prácticas de Consultas SQL - DVD Rental Database

Colección de ejercicios prácticos de consultas SQL utilizando la base de datos PostgreSQL **dvdrental**.

## Base de Datos

**dvdrental** es una base de datos de ejemplo que simula el sistema de una tienda de renta de películas DVD. Contiene información sobre películas, clientes, alquileres, actores, categorías y más.

### Esquema Principal

| Tabla       | Descripción                                                     |
| ----------- | --------------------------------------------------------------- |
| `film`      | Catálogo de películas con título, descripción, duración, tarifa |
| `customer`  | Datos de clientes (nombre, apellido, email)                     |
| `rental`    | Registros de alquiler con fechas                                |
| `inventory` | Inventario de películas disponibles                             |
| `actor`     | Actores                                                         |
| `category`  | Categorías de películas                                         |
| `payment`   | Pagos realizados                                                |

## Archivos de Práctica

### 01_analisis_catalogo.sql

Análisis del catálogo de películas.

**Objetivo:** Seleccionar películas con tarifa entre 3 y 5 que contengan "action" en su descripción.

```sql
SELECT title, description, rental_rate
FROM film
WHERE description ILIKE '%action%'
    AND rental_duration BETWEEN 3 AND 5
ORDER BY rental_rate DESC
LIMIT 5;
```

**Conceptos:** `WHERE`, `LIKE/ILIKE`, `BETWEEN`, `ORDER BY`, `LIMIT`

---

### 02_comunicacion_con_clientes.sql

Comunicación con clientes.

**Objetivo:** Obtener datos de clientes que rentaron películas en una fecha específica.

```sql
SELECT
    customer.first_name,
    customer.last_name,
    customer.email,
    rental.rental_date
FROM customer
INNER JOIN rental ON customer.customer_id = rental.customer_id
WHERE CAST(rental.rental_date AS DATE) = '2005-05-24'
ORDER BY last_name ASC;
```

**Conceptos:** `JOIN`, `CAST`, filtrado por fecha

---

### 03_audotoria_inventario.sql

Auditoría de inventario.

**Objetivo:** Identificar películas que están registradas en el catálogo pero no tienen inventario disponible (LEFT JOIN con valor NULL).

```sql
SELECT
    film.film_id,
    film.title
FROM film
LEFT JOIN inventory ON film.film_id = inventory.film_id
WHERE inventory.inventory_id IS NULL
ORDER BY film.film_id ASC;
```

**Conceptos:** `LEFT JOIN`, valores NULL, auditoría de datos

---
