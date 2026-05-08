# Resumen Completo — Módulo 4: Modelos y Gestión de Bases de Datos
**Diplomado en Data Engineer — USACH**  
**Docente:** José Luis Martí Lara (Ingeniero Civil Informático, UTFSM | Máster en Diseño de Información y Visualización de Datos, UPF)

---

> **Cómo usar este resumen:** Cubre las 5 clases del módulo. Está diseñado para ser suficientemente completo como para estudiar sin las diapositivas originales. Donde el material gráfico fue significativo (diagramas de modelos, comparativas), se reconstruye el contenido de forma descriptiva y se complementa con contexto técnico profesional.

---

# CLASE 1 — Introducción a Bases de Datos, Semántica de Datos y Diseño Conceptual

## 1. Fundamentos: Datos, Información y Archivos

### Dato
Un **dato** es un hecho relacionado con personas, objetos, lugares, eventos u otras entidades del mundo real. Representa la unidad mínima de información cruda, sin contexto.

- Las organizaciones dependen completamente de sus datos.
- El dato es un **activo corporativo crítico** y debe ser gestionado como tal.

### Información
La **información** son datos organizados, procesados y formateados de una manera adecuada para la toma de decisiones u otras actividades organizacionales.

> El paso de dato a información es **subjetivo**: el mismo dato puede ser información para una persona y ruido para otra. Su valor depende del contexto y el usuario.

### Archivo
Un **archivo** es un conjunto de datos relacionados entre sí, que comparten una misma estructura o comportamiento similar. Cada entidad representada en el archivo se guarda en un **Registro**.

Un archivo puede clasificarse según su clave:

| Tipo de Clave | Descripción |
|---|---|
| **Clave Simple** | Contiene un único atributo identificador |
| **Clave Compuesta** | Contiene más de un atributo identificador |
| **Clave Candidata** | Atributo con valor único dentro del archivo (candidato a PK) |
| **Clave Primaria (PK)** | Clave candidata escogida como la principal |
| **Clave Alternativa** | Clave candidata no escogida como primaria |
| **Clave Secundaria** | Atributo que puede contener valores repetidos (no identifica de forma única) |

---

## 2. Bases de Datos: Definición y Características

Una **Base de Datos** es un conjunto integrado de archivos relacionados entre sí, diseñados para ser accesados por numerosos usuarios a través de distintos medios.

### Características principales:
- **Visión centralizada de los datos:** una sola fuente de verdad.
- **Minimización de la redundancia:** los datos no se duplican innecesariamente.
- **Independencia de los datos:** la estructura lógica se separa de la física; cambios internos no afectan las aplicaciones.
- **Estandarización, compartición y seguridad:** acceso controlado y uniforme.

---

## 3. Clasificación de Bases de Datos

El curso propone una taxonomía multidimensional de bases de datos según cuatro criterios:

### Criterio 1: Inteligencia de los Datos
Evalúa cómo se estructuran los datos y sus relaciones.

**Subcriterio 1: Modelo de Datos (complejidad de representación):**
- **Jerárquico:** árbol padre-hijo (ej.: IMS de IBM). Rígido, navegación predefinida.
- **Reticular (red):** permite relaciones muchos-a-muchos directas entre registros.
- **Relacional:** tablas, claves foráneas, álgebra relacional. El dominante en la industria por décadas.
- **Orientado al Objeto:** encapsula datos y comportamiento. Permite herencia y polimorfismo en el modelo de datos.
- **Multidimensional:** estructura en torno a dimensiones (tiempo, producto, región) y métricas. Base del OLAP.

**Subcriterio 2: Expresividad de tipos (precisión y estructuración):**
- **Estructurada:** esquema rígido y bien definido (ej.: SQL).
- **SemiEstructurada:** esquema flexible, los datos llevan información sobre su propia estructura (ej.: JSON, XML).
- **No Estructurada:** texto libre, imágenes, audio.
- **Multimedios:** almacena imágenes, audio, video.
- **Espacial/Geográfica:** datos con coordenadas y geometría.
- **Difusa:** maneja incertidumbre e imprecisión (ej.: "color del medicamento puede ser blanco, rojo, amarillo o naranja con cierta intensidad").
- **Deductiva/Estadística:** permite inferir nuevo conocimiento a partir de reglas.

### Criterio 2: Distribución e Integración
- **Centralizada vs. Distribuida:** los datos residen en un nodo o en múltiples nodos geográficamente separados.
- **En la web / Móvil:** con autonomía limitada o sin red permanente.
- **Federada:** múltiples bases heterogéneas que se presentan como una sola.

### Criterio 3: Rendimiento
- **Serial (monoprocesador) vs. Paralela:** múltiples CPUs procesando consultas en paralelo.
- **Basada en disco vs. Basada en memoria principal (in-memory):** Redis, Memcached operan completamente en RAM para latencias de microsegundos.
- **En Tiempo Real:** restricciones duras sobre latencia de respuesta (ej.: sistemas de control industrial).

### Criterio 4: Nivel Organizacional que Apoya

| Nivel | Tipo de BD | Característica |
|---|---|---|
| Operacional | OLTP (Transaccional) | Alta concurrencia, operaciones CRUD, integridad ACID |
| Táctico | OLAP / Data Mart | Consultas analíticas, agregaciones sobre subconjuntos del negocio |
| Estratégico | Data Warehouse | Integración histórica de toda la organización para soporte a decisiones |

> **Analogía útil:** OLTP es el "día a día" (vender, registrar, cobrar). OLAP es el "análisis" (¿cuánto vendí el último trimestre?). DW es el "repositorio histórico integrado" (todos los datos de todas las áreas, históricamente).

### Bases de Datos NoSQL
Categoría muy amplia para un grupo de soluciones de persistencia que **no siguen el modelo relacional** y **no usan SQL como lenguaje de consulta**. Se profundiza en clases posteriores.

---

## 4. Proceso de Diseño de Bases de Datos

El diseño de una base de datos sigue un proceso iterativo de 6 etapas:

### Etapa 1: Recolección y Análisis de Requisitos
**Objetivo:** Identificar las necesidades de información de los usuarios. Se trabaja con entrevistas, documentos existentes, observación de procesos.

### Etapa 2: Diseño Conceptual
**Objetivo:** Producir un esquema conceptual que represente los datos necesarios, **independiente del motor a utilizar**.

Ejemplo: Un modelo con entidades `Cliente`, `Factura`, `Producto` con sus atributos (sin definir tipos de datos ni claves foráneas explícitas, solo relaciones semánticas).

```
Cliente ──── Factura ──── Producto
RUT          #factura      #producto
Nombre       Fecha         Nombre
Teléfono                   Precio
```

### Etapa 3: Elección del Software
**Objetivo:** Seleccionar el tipo de DBMS (relacional, documental, grafos, etc.) que mejor se adecúe a los requisitos funcionales y no funcionales (rendimiento, escala, presupuesto).

### Etapa 4: Diseño Lógico
**Objetivo:** Transformar el esquema conceptual al **modelo de datos del software escogido**.

Para el modelo relacional, se aplican las reglas de transformación de entidad-relación a tablas.

```
Conceptual:                   Relacional:
Cliente – Factura – Producto  Cliente(RUT PK, Nombre, Teléfono)
                              Factura(#factura PK, Fecha, RUT FK)
                              Detalle(#factura FK, #producto FK, cantidad)
                              Producto(#producto PK, Nombre, Precio)
```

### Etapa 5: Diseño Físico
**Objetivo:** Escoger las estructuras de almacenamiento, métodos de acceso, índices y ubicación de archivos para **obtener buen rendimiento**.

```sql
-- Del modelo lógico al físico:
CREATE TABLE cliente (
    RUT        CHAR(9)     PRIMARY KEY,
    Nombre     VARCHAR(35) NOT NULL,
    Direccion  VARCHAR(50),
    Sexo       CHAR
);
```

### Etapa 6: Implementación
**Objetivo:** Codificación SQL (DDL + DML) para crear los archivos y poblarlos con datos iniciales.

---

## 5. Semántica de los Datos

Un modelo de datos es una **abstracción de la realidad**. Cada modelo tiene restricciones sobre la semántica que puede representar. La semántica de los datos se refiere al **significado de las relaciones entre datos**.

El curso usa la notación de **Diagramas de Clase UML** para representar estas semánticas.

### a) Cardinalidad (Multiplicidad)
Número de entidades con que otra entidad se relaciona.

| Tipo | Notación UML | Ejemplo |
|---|---|---|
| Uno a uno (1:1) | `1 — 1` | Empleado – Cónyuge (obligatoria opcional: `1 — 0..1`) |
| Uno a muchos (1:N) | `1 — *` | Persona – Automóvil (una persona puede tener varios autos) |
| Muchos a muchos (M:N) | `* — *` | Curso – Alumno (con mínimos: `1..* — 1..*`) |

La cardinalidad incluye la propiedad de **obligatoriedad/opcionalidad**:
- `0..1` → opcional (puede o no existir)
- `1` → obligatorio exactamente uno
- `*` → cero o más
- `1..*` → uno o más

### b) Grado
Número de **tipos de entidades** que participan en una asociación.

| Grado | Descripción | Ejemplo |
|---|---|---|
| **Unaria** | Una entidad se relaciona consigo misma | `Cargo supervisa Cargo` |
| **Binaria** | Dos tipos de entidades | `Persona — Automóvil` |
| **Ternaria** | Tres tipos de entidades | `Producto — Bodega — Pedido` |
| **n-aria** | n tipos de entidades | Poco común, suele descomponerse |

### c) Dependencia Existencial
Una entidad no puede existir sin la presencia de otra. Formaliza el concepto de **entidad débil**.

- Beneficio: garantiza **integridad referencial** y facilita el acceso a la entidad dependiente.
- Ejemplo: un `Ítem de Factura` no puede existir sin su `Factura`.

### d) Tiempo
Variación del contenido de la base de datos respecto al tiempo.

**Estampillas de Tiempo:** atributo que indica el momento o intervalo de validez de los valores almacenados.
- Ejemplos: `Fecha de Pago`, `Fecha de Contrato`, `Fecha de Inicio – Fecha de Fin`.

**Restricciones de Inserción y Retención:**
- **Inserción:** instante en que el dato puede ingresarse, antes o después de la presencia de otro dato relacionado.
- **Retención:** período de tiempo durante el cual tiene sentido registrar una relación.

### e) Unicidad
Asociado con la presencia única de un dato, objeto o relación.

**Unicidad por Identificador:** necesidad de tener un valor único para cada ocurrencia de entidad (implementado como `PRIMARY KEY`).

```
Persona
RUT {ID}
Nombre
Domicilio
```

**Exclusividad:** solo puede estar presente un tipo de dato o relación, de entre varios posibles.
```
Persona — {OR} — Empresa
         Automóvil
```
(Un automóvil pertenece a una Persona O a una Empresa, nunca a ambas)

### f) Herencia
Permite ver un conjunto de entidades con propiedades similares como un mismo tipo de entidad. Corresponde a la relación "**es un(a)**".

- **Supertipo (superclase):** el tipo más general.
- **Subtipo (subclase):** subconjunto de la superclase que reutiliza sus propiedades y agrega las propias.

**Las tres propiedades de la herencia:**

| Propiedad | Significado |
|---|---|
| **Cobertura** | Si todas las instancias de la superclase pertenecen a al menos una subclase → cobertura *total* (exhaustiva) |
| **Exclusividad** | Si una entidad pertenece solo a una subclase a la vez → jerarquía *exclusiva* |
| **Dinamicidad** | Si una entidad puede cambiar de subclase → jerarquía *dinámica* |

### g) Agregación
Colección de entidades de **diferentes tipos**. Corresponde a la relación "**todo – partes**". El objeto compuesto agrupa las partes.

- Ejemplo: `Computador` agrega `CPU`, `RAM`, `Disco`.
- Diferencia con herencia: en la herencia un subtipo "**es**" el supertipo; en la agregación una parte "**tiene**" o "**compone**" al todo.

### h) Categorización
Modela una relación de clases que tienen diferentes tipos de datos. Es una semántica de diseño avanzada (no se utiliza en el resto del curso).

### Semántica Adicional: Clases de Asociación
Cuando una asociación tiene sus propios atributos, se modela como una **clase de asociación**. Ejemplo: `Trabajador — trabaja_para — Organización` con el atributo `rol`.

---

## 6. Diseño Conceptual: Ejercicio Práctico

El curso presenta el siguiente problema para aplicar todo lo visto:

**Problema: Campeonato Mundial de Fórmula 1**

> Los pilotos firman contratos para correr durante una temporada en los autos de una escudería. Una escudería puede tener varios pilotos (mínimo uno). Cada escudería pertenece a un país. Los automóviles se inscriben en una escudería y se asignan a pilotos por carrera. Un piloto usa solo un automóvil por carrera. En una temporada se realizan muchas carreras en circuitos. Un circuito puede tener varias carreras en distintas temporadas. Un circuito puede estar en reparaciones sin carreras programadas.

**Entidades identificadas:** Piloto, Escudería, País, Automóvil, Temporada, Carrera, Circuito.

**Relaciones clave:**
- `Piloto — contrato — Escudería` (M:N, para una temporada)
- `Escudería — pertenece — País` (M:1)
- `Automóvil — inscrito — Escudería` (M:1)
- `Piloto — usa — Automóvil` (en una Carrera específica → relación ternaria)
- `Carrera — se_realiza_en — Circuito` (M:1)
- `Carrera — pertenece — Temporada` (M:1)

---

# CLASE 2 — Bases de Datos Relacionales y SQL

## 1. El Modelo Relacional

### Características fundamentales
- **Independencia física de los datos:** la representación lógica (tablas) es independiente del almacenamiento físico.
- **Claves lógicas:** las relaciones entre entidades se expresan con claves (primarias y foráneas), no con punteros físicos.
- **Teoría de la normalización:** conjunto de reglas formales para eliminar redundancias y anomalías.
- **Lenguaje de consultas de alto nivel:** SQL, que abstrae el cómo y permite expresar el qué.

### Terminología básica

| Término Relacional | Equivalente Intuitivo | Descripción |
|---|---|---|
| Relación / Tabla | Archivo | Estructura bidimensional de datos |
| Tupla / Fila | Registro | Una instancia de la entidad |
| Atributo / Columna | Campo | Característica medible de la entidad |
| Dominio | Conjunto de valores válidos | Tipo de dato + restricciones del atributo |
| Clave Primaria (PK) | Identificador único | No permite valores nulos ni repetidos |
| Clave Foránea (FK) | Referencia | Atributo que referencia la PK de otra tabla |

**Reglas importantes:**
- El orden de las filas es irrelevante (una relación es un conjunto).
- Cada fila es única (garantizada por la PK).
- Cada columna contiene valores del mismo dominio.

---

## 2. Transformación del Modelo Conceptual al Relacional (Diseño Top-Down)

El proceso de transformación sigue **7 pasos canónicos**:

### Paso 1: Entidades Fuertes → Tablas
Por cada entidad fuerte: crear una tabla con todos sus atributos simples. Escoger la clave candidata como PK.

```
Conceptual: Entidad CLIENTE (RUT, Nombre, Dirección, Sexo)
Relacional: CLIENTE(RUT PK, Nombre, Dirección, Sexo)
```

### Paso 2: Entidades Débiles → Tablas con PK Compuesta
Una **entidad débil** existe solo en función de una entidad fuerte F. Su PK es la concatenación de la PK de F con su propio identificador parcial.

```
Entidad débil A depende de F(IdF):
A(IdF FK, IdA, atributos_A)
PK = (IdF, IdA)
```

> **Intuición:** un `Ítem de Factura` no tiene sentido sin una `Factura`. Su PK sería `(#Factura, #Ítem)`.

### Paso 3: Asociaciones 1:1
Identificar las dos tablas involucradas; incluir la PK de una como FK en la otra. Se elige el lado con menor impacto de NULLs.

### Paso 4: Asociaciones 1:N
La FK va en el lado **N** (la tabla del lado "muchos" incluye la PK del lado "uno"). Incluir cualquier atributo de la asociación en el lado N.

```
PERSONA(RUT PK, Nombre)
AUTOMOVIL(Placa PK, Marca, RUT_Propietario FK → PERSONA)
```

### Paso 5: Asociaciones M:N → Tabla de Intersección
Crear una **nueva tabla** que representa la asociación. Sus atributos son las PKs de ambas entidades (ambas como FKs) más los atributos propios de la relación. La PK suele ser la combinación de ambas FKs.

```
Conceptual: ALUMNO (M:N) CURSO
Relacional:
  ALUMNO(RUT PK, Nombre)
  CURSO(CodCurso PK, Nombre)
  MATRICULA(RUT FK, CodCurso FK, Fecha, Nota)  ← tabla de intersección
  PK = (RUT, CodCurso)
```

### Paso 6: Asociaciones n-arias
Crear una nueva tabla que incluye las PKs de todas las entidades participantes como FKs. La PK suele ser la concatenación de todas ellas.

```
Conceptual: PRODUCTO — BODEGA — PEDIDO (ternaria)
Relacional: STOCK(CodProducto FK, CodBodega FK, CodPedido FK, Cantidad)
```

### Paso 7: Herencia — Cuatro Alternativas

Dada la jerarquía: superclase `A` con subclases `B` y `C`:

#### Alternativa 1: Superclase y Subclases "sobreviven"
Crear una tabla para la superclase y una por cada subclase. La PK de la subclase es la PK de la superclase (también FK).

```sql
-- Superclase
CREATE TABLE A (IdA PK, atrib_comunes);

-- Subclases (IdA es PK y FK simultáneamente)
CREATE TABLE B (IdA PK FK → A, atrib_propios_B);
CREATE TABLE C (IdC PK, IdA FK → A, atrib_propios_C);
```

**Cuándo usarla:** Herencia parcial o cuando las subclases tienen muchos atributos propios diferentes.

#### Alternativa 2: Subclases "absorben" a la superclase
Una tabla por subclase, cada una incluye todos los atributos de la superclase más sus propios.

```sql
CREATE TABLE B (IdA PK, atrib_comunes_de_A, atrib_propios_B);
CREATE TABLE C (IdC PK, atrib_comunes_de_A, atrib_propios_C);
```

**Cuándo usarla:** Herencia total y exclusiva, sin instancias de la superclase pura.

#### Alternativa 3.1: Superclase "absorbe" a las subclases (herencia exclusiva)
Una única tabla con todos los atributos más un **discriminador** que indica a qué subclase pertenece.

```sql
CREATE TABLE A (
    IdA PK,
    atrib_comunes,
    tipo CHAR,          -- discriminador: 'B' o 'C'
    atrib_de_B NULL,    -- NULL cuando tipo = 'C'
    atrib_de_C NULL     -- NULL cuando tipo = 'B'
);
```

**Cuándo usarla:** Herencia exclusiva, pocas subclases, pocos atributos propios.

#### Alternativa 3.2: Superclase "absorbe" a las subclases (herencia no exclusiva)
Similar a 3.1, pero con **flags booleanos** en lugar de un discriminador único.

```sql
CREATE TABLE A (
    IdA PK,
    atrib_comunes,
    es_B BOOLEAN,
    es_C BOOLEAN,
    atrib_de_B NULL,
    atrib_de_C NULL
);
```

**Cuándo usarla:** Una entidad puede pertenecer a múltiples subclases simultáneamente.

---

## 3. Documentación Adicional del Diseño

El modelo de datos describe las **reglas estáticas** del negocio. Pero hay aspectos complementarios importantes:

### Desnormalización
Agregar **redundancia controlada** al modelo relacional normalizado para mejorar el rendimiento de consultas frecuentes.

- **Trade-off:** mejor rendimiento de lectura vs. menor integridad (requiere código adicional para mantener consistencia).
- **Ejemplo:** almacenar el `total` calculado en la tabla `Pedido` en lugar de calcularlo siempre con `SUM(precio * cantidad)`.
- **Patrón:** "Almacenar Valores Derivados" — agregar columnas calculadas en el extremo referenciado de la FK.

> **Cuándo desnormalizar:** en sistemas OLAP/DW donde las lecturas superan masivamente las escrituras. Evitar en OLTP donde la integridad es crítica.

### Descripción de Archivos (Diccionario de Datos)
Documentar para cada tabla: nombre del atributo, tipo de dato, longitud, restricciones, descripción funcional, si es PK/FK. Herramienta fundamental para el mantenimiento del sistema.

### Reglas Dinámicas del Negocio (Triggers y SP)
Especificaciones que preservan la integridad del modelo ante eventos DML. Un trigger se documenta con:
- **Regla de usuario:** descripción concisa de la regla.
- **Evento:** operación DML que lo activa (INSERT, UPDATE, DELETE).
- **Entidad:** tabla sobre la que actúa.
- **Condición:** cuándo se gatilla.
- **Acción:** qué hace cuando se activa.

---

## 4. SQL: Lenguaje de Consulta para Bases de Datos Relacionales

SQL es el **lenguaje estándar** para consultar bases de datos relacionales (PostgreSQL, MySQL, MS SQL Server, etc.).

### Ejemplo de Esquema del Curso

```sql
CREATE TABLE autores (
    id_autor      INT PRIMARY KEY,
    nombre        VARCHAR(100) NOT NULL,
    nacionalidad  VARCHAR(50)
);

CREATE TABLE libros (
    id_libro         INT PRIMARY KEY,
    titulo           VARCHAR(150) NOT NULL,
    anio_publicacion INT,
    id_autor         INT,
    FOREIGN KEY (id_autor) REFERENCES autores(id_autor)
);

-- Índice para optimizar consultas por autor
CREATE INDEX idx_libros_autor ON libros(id_autor);
```

### Consultas Cubiertas en Clase

```sql
-- C1: Todos los libros
SELECT * FROM libros;

-- C2: Filtrado con WHERE
SELECT titulo, anio_publicacion
FROM libros
WHERE anio_publicacion > 2015;

-- C3: Búsqueda parcial con LIKE
SELECT *
FROM libros
WHERE titulo LIKE '%historia%';

-- C4: JOIN entre tablas
SELECT l.titulo, l.anio_publicacion, a.nombre AS autor
FROM libros l
JOIN autores a ON l.id_autor = a.id_autor;

-- C5: Agregación con GROUP BY (LEFT JOIN para incluir autores sin libros)
SELECT a.nombre, COUNT(l.id_libro) AS total_libros
FROM autores a
LEFT JOIN libros l ON a.id_autor = l.id_autor
GROUP BY a.nombre;

-- C6: Filtro sobre grupos con HAVING
SELECT a.nombre, COUNT(l.id_libro) AS total_libros
FROM autores a
JOIN libros l ON a.id_autor = l.id_autor
GROUP BY a.nombre
HAVING COUNT(l.id_libro) > 2;

-- C7: Subconsulta correlacionada
SELECT titulo
FROM libros
WHERE id_autor = (
    SELECT id_autor
    FROM libros
    GROUP BY id_autor
    ORDER BY COUNT(*) DESC
    LIMIT 1
);
```

> **Nota profesional sobre el índice:** `CREATE INDEX idx_libros_autor ON libros(id_autor)` acelera drásticamente las consultas C4–C7, pues el optimizador puede hacer un **index scan** en lugar de un **full table scan** para encontrar libros de un autor específico.

---

# CLASE 3 — Bases de Datos NoSQL: Fundamentos, Clave-Valor y Columnas Anchas

## 1. Introducción a NoSQL

**Definición:** Categoría muy amplia para un grupo de soluciones de persistencia que:
1. **No siguen el modelo de datos relacional.**
2. **No usan SQL como lenguaje de consulta** (algunos tienen lenguajes similares a SQL).

> El término "NoSQL" es algo equívoco. Modernamente se interpreta como "Not Only SQL" — muchos sistemas NoSQL sí tienen capacidades similares a SQL. La característica definitoria es la flexibilidad de esquema y el diseño orientado a escala horizontal.

### Los cuatro grandes tipos de bases de datos NoSQL

| Tipo | Modelo de Datos | Ejemplos | Caso de Uso Ideal |
|---|---|---|---|
| **Clave-Valor** | Pares `clave → valor` | Redis, Riak, DynamoDB | Caché, sesiones, preferencias de usuario |
| **Columnas Anchas** (Wide Column) | Tablas con columnas variables por fila | Cassandra, HBase | Series temporales, logs a escala masiva |
| **Documental** | Documentos JSON/XML | MongoDB, CouchBase | APIs web, catálogos, contenido variable |
| **Grafos** | Nodos, aristas y propiedades | Neo4j, InfiniteGraph | Redes sociales, recomendaciones, rutas |

---

## 2. ACID vs. BASE y el Teorema CAP

Este es el **núcleo conceptual fundamental** para entender por qué existen los sistemas NoSQL.

### Propiedades ACID (Bases de Datos Relacionales)

| Propiedad | Descripción |
|---|---|
| **A**tomicidad | Una transacción se ejecuta por completo o no se ejecuta. Si falla en algún paso, se revierte (rollback). |
| **C**onsistencia | La ejecución de una transacción lleva la BD de un estado válido a otro estado válido (respetando todas las reglas y restricciones). |
| **I**solamiento (Isolation) | Las transacciones concurrentes se ejecutan sin interferirse entre sí, como si fueran secuenciales. |
| **D**urabilidad | Una vez confirmada (commit), la transacción persiste incluso ante fallos del sistema (está en disco). |

> ACID es la razón por la que confías en que tu transferencia bancaria no se pierda. Pero garantizarlo en sistemas distribuidos es **extremadamente costoso** en términos de coordinación de nodos.

### Propiedades BASE (Bases de Datos NoSQL Distribuidas)

| Propiedad | Descripción |
|---|---|
| **B**asically Available | El sistema garantiza disponibilidad. Aunque falle un nodo, la BD responde (quizás con datos no 100% actualizados). |
| **S**oft State | El estado puede cambiar con el tiempo sin interacción directa, por la sincronización entre nodos. |
| **E**ventual Consistency | Los datos no son consistentes de inmediato en todos los nodos, pero *eventualmente* todos convergerán al mismo estado. |

> **Analogía:** si actualizas tu foto de perfil en WhatsApp, algunos contactos la ven de inmediato y otros la ven actualizada horas después. El sistema estaba "eventualmente consistente".

### Teorema CAP (Brewer, 2000)

Un sistema distribuido **solo puede garantizar 2 de las siguientes 3 propiedades simultáneamente**:

```
         Consistencia
            /\
           /  \
          /    \
         /      \
        /--------\
Disponibilidad  Tolerancia a
                  Particiones
```

| Propiedad | Descripción |
|---|---|
| **C**onsistencia | Todo usuario tiene una visión idéntica de los datos en cualquier instante. |
| **A**vailability (Disponibilidad) | La BD se mantiene operativa aunque caiga algún nodo. |
| **P**artition Tolerance (Tolerancia a Particiones) | La BD mantiene operación aunque segmentos del sistema distribuido fallen (red particionada). |

**Implicaciones prácticas:**
- En la práctica, en internet la **tolerancia a particiones es no negociable** (los nodos se desconectan inevitablemente).
- Por lo tanto, la elección real es entre **CP** (consistencia + tolerancia) o **AP** (disponibilidad + tolerancia).
- Los sistemas relacionales tradicionales son **CA** (pero asumen un único nodo o red confiable).

| Clasificación | Ejemplos | Trade-off |
|---|---|---|
| **CA** (C + A) | PostgreSQL, MySQL | Sin particiones distribuidas reales |
| **CP** (C + P) | MongoDB, HBase, Zookeeper | Puede rechazar peticiones bajo partición |
| **AP** (A + P) | Cassandra, CouchDB, DynamoDB | Devuelve datos posiblemente desactualizados |

---

## 3. Tipos de Consistencia

NoSQL introduce consistencia ajustable como concepto clave:

### Consistencia Eventual
Tras un cambio, eventualmente todos los accesos retornarán el valor más actualizado. La ventana de inconsistencia puede variar de milisegundos a segundos.

### Consistencia Estricta
Todo cambio se propaga a todos los nodos de forma sincrónica e inmediata antes de confirmar la escritura. Garantiza que ningún cliente lee datos "viejos".

### Consistencia Sintonizable (Tunable Consistency)
Usada por **Cassandra, CouchDB, Azure Cosmos DB**. Permite que la aplicación elija el nivel de consistencia para cada operación, usando la notación **NWR**:

- **N:** número total de réplicas del dato.
- **W:** número de réplicas que deben confirmar la escritura antes de retornar éxito.
- **R:** número de réplicas que deben responder a una lectura.

**Regla de consistencia fuerte:** `W + R > N`

| Configuración | Efecto | Uso |
|---|---|---|
| N=3, W=3, R=1 | Escritura lenta, lectura rápida y consistente | Datos críticos |
| N=3, W=1, R=3 | Escritura rápida, lectura lenta con verificación | Logs con validación |
| N=3, W=1, R=1 | Máxima velocidad, consistencia eventual | Métricas/telemetría |
| N=3, W=2, R=2 | Balance (quórum) | Caso de uso general |

---

## 4. Bases de Datos Clave-Valor

### Concepto
Almacena datos como pares `clave → valor`. La clave es un identificador único; el valor puede ser cualquier cosa (string, número, JSON, binario).

```
"user123"     → "Juan Pérez"
"session456"  → {"token": "abc", "expira": "2026-01-01"}
"config:timeout" → 30
```

### Ventajas y Limitaciones

| Ventajas | Limitaciones |
|---|---|
| Muy rápidas (O(1) en acceso) | No permiten consultas complejas sobre el valor |
| Simples de usar | No hay relaciones entre datos |
| Escalables horizontalmente | No sirven para análisis o búsquedas avanzadas |
| Ideales para acceso directo por clave | El valor es opaco (la BD no lo "entiende") |

### Casos de Uso Reales
- **Caché de sesiones:** almacenar tokens JWT con TTL.
- **Configuración distribuida:** feature flags, parámetros de aplicación.
- **Contadores distribuidos:** likes, visitas (con operaciones atómicas INCR en Redis).
- **Pub/Sub:** Redis como broker de mensajes ligero.
- **Cola de trabajo:** Redis Lists como cola FIFO.

### Redis: El referente del mercado
- In-memory con persistencia opcional (RDB + AOF).
- Estructuras de datos ricas: Strings, Lists, Sets, Sorted Sets, Hashes, Streams.
- Soporta TTL nativo (fundamental para cachés).

---

## 5. Bases de Datos de Columnas Anchas (Wide Column Stores)

### Distinción importante
El curso distingue dos conceptos diferentes que suelen confundirse:

| Concepto | Descripción | Ejemplo |
|---|---|---|
| **BD orientada a columnas** | Almacena los datos por columna en vez de por fila. No necesariamente NoSQL. | HPE Vertica Analytics |
| **BD de columnas anchas (Wide Column)** | NoSQL. Soporta tablas donde cada fila puede tener diferente número y tipo de columnas. | Cassandra, HBase |

### Por qué el almacenamiento columnar es mejor para OLAP

```
Tabla por filas (row-oriented):
Fila 1: [1, 1, 2001-01-01, Smith, Bob]
Fila 2: [2, 1, 2002-02-01, Jones, Jim]
Fila 3: [3, 1, 2002-05-01, Young, Sue]

Para calcular SUM(salario): se deben leer TODAS las filas completas.

Tabla por columnas (column-oriented):
Columna Emp_no: [1, 2, 3, 4, 5, 6]
Columna Dept_id: [1, 1, 1, 2, 2, 3]
Columna salario: [2000, 3000, 2500, 4000, 3500, 2800]

Para calcular SUM(salario): solo se lee la columna salario.
→ Mucho menos I/O en disco para agregaciones.
```

**Ventajas adicionales del almacenamiento columnar:**
- **Compresión:** valores similares en la misma columna se comprimen mejor (ej.: run-length encoding en columnas de bajo cardinality).
- **Proyecciones:** para consultas de una sola columna, la columna aislada es suficiente. Para consultas multicolumna, se precalculan **proyecciones** (vistas materializadas de combinaciones frecuentes).

**Desventaja para OLTP:**
- Insertar/actualizar un registro requiere escribir en múltiples archivos (uno por columna) → overhead en escrituras.
- Solución: usar un **almacén delta** (buffer de escritura en memoria) que se fusiona periódicamente con las columnas (Vertica lo llama "Tuple Mover"; Sybase IQ usa Row Level Versioned).

### Ventajas y Limitaciones de Wide Column

| Ventajas | Limitaciones |
|---|---|
| Alta disponibilidad y escalabilidad horizontal | No diseñadas para consultas complejas ad-hoc |
| Flexibilidad de esquema (filas con columnas distintas) | No soportan JOINs nativos |
| Eficiente almacenamiento y compresión | Sin integridad referencial |
| Consultas de agregación rápidas | El modelado debe orientarse a consultas |

---

## 6. Caso de Estudio: Apache Cassandra

Cassandra es el referente de Wide Column Stores en producción. Usada por Netflix, Discord, Facebook, Instagram.

### Arquitectura del Modelo de Datos

La jerarquía de almacenamiento en Cassandra:

```
Cluster
  └── KeySpace (≈ base de datos)
        └── Table (≈ tabla, pero orientada a consultas)
              └── Partition (grupo de filas con misma clave de partición)
                    └── Row (fila, referenciada por clave primaria)
                          └── Column (par nombre/valor)
```

**Detalles clave:**
- **Columna:** par nombre/valor.
- **Fila:** contenedor de columnas, referenciada por una clave primaria.
- **Partición:** grupo de filas relacionadas almacenadas juntas en los mismos nodos físicos.
- **Tabla:** contenedor de filas organizadas por particiones.
- **KeySpace:** contenedor de tablas, equivalente a una base de datos. Define la estrategia de replicación.

### Filosofía de Diseño: Query-First

> En el modelo relacional, el diseño comienza con el modelo conceptual (entidades y relaciones) y luego se traduce a tablas. En Cassandra, el diseño **comienza por las consultas** y los datos se organizan en torno a ellas.

**Principios fundamentales:**
- **No hay JOINs:** si necesitas datos relacionados, debes desnormalizar (tablas diseñadas específicamente para cada consulta).
- **No hay integridad referencial:** las eliminaciones en cascada no existen; la consistencia debe gestionarse en la aplicación.
- **Minimizar el número de particiones accedidas:** el objetivo clave es que una consulta acceda a la menor cantidad de particiones posible.
- **El ordenamiento es una decisión de diseño:** las columnas de clustering definen el orden de filas dentro de una partición.

### Diseño de Tablas: Ejemplo de Clientes y Pedidos

**Mal diseño (imitando el modelo relacional):**
```sql
-- Estructura anidada, no escalable
CREATE TABLE customer (
    id    INT PRIMARY KEY,
    name  TEXT,
    orders LIST<FROZEN<myorder>>  -- problemático para actualizaciones
);
```

**Buen diseño (orientado a consultas):**
```sql
-- Consulta 1: Ver pedidos de un cliente
CREATE TABLE orders_by_customer (
    customer_id   INT,
    customer_name TEXT,
    order_no      TEXT,
    order_date    TIMESTAMP,
    PRIMARY KEY (customer_id, order_no)
    -- customer_id: clave de partición
    -- order_no: columna de clustering (define orden dentro de la partición)
);

-- Consulta 2: Ver todos los productos de un pedido
CREATE TABLE order_lines_by_order (
    order_no      TEXT,
    product_no    TEXT,
    product_name  TEXT,
    price         DECIMAL,
    PRIMARY KEY (order_no, product_no)
);

-- Tabla desnormalizada que responde ambas consultas:
CREATE TABLE orders_full_by_customer (
    customer_id   INT,
    customer_name TEXT,
    order_no      TEXT,
    product_no    TEXT,
    product_name  TEXT,
    price         DECIMAL,
    PRIMARY KEY (customer_id, order_no, product_no)
);
```

### Configuración de KeySpace con Replicación

```sql
CREATE KEYSPACE myspace
WITH REPLICATION = {
    'class': 'SimpleStrategy',
    'replication_factor': 3  -- 3 copias de cada dato
};
```

> `SimpleStrategy` para desarrollo o un solo datacenter. `NetworkTopologyStrategy` para producción multi-datacenter.

### Proceso de Diseño en Cassandra (8 Pasos del Ejemplo Hotel)

1. **Modelo conceptual:** identificar entidades (Hotel, Habitación, Huésped, Reserva, etc.) y relaciones.
2. **Identificar consultas:** ej. "ver habitaciones disponibles por hotel y fecha", "ver reservas por huésped".
3. **Construir el grafo de navegación:** mapa visual de qué consulta usa qué datos.
4. **Modelo lógico:** usar notación de Chebotko para definir tablas con sus claves de partición y clustering.
5. **Modelo físico:** traducir al CQL concreto con tipos de datos.
6. **Revisión de patrones de acceso:** validar que cada consulta accede a una sola partición.

---

# CLASE 4 — Bases de Datos Documentales (MongoDB)

## 1. Bases de Datos Documentales: Concepto

Una **base de datos documental** almacena datos como documentos semi-estructurados, usualmente en formato **JSON** o **XML**.

A diferencia del modelo relacional donde los datos y su definición están separados (esquema vs. datos), en el modelo documental los datos **se intercalan con tags estructurales** que definen su estructura, anidamiento y tipo.

### ¿Por qué surgieron?
- **Limitaciones del modelo relacional:** esquemas rígidos, JOINs costosos, impedance mismatch con lenguajes OO.
- **Necesidad de manejar datos semi-estructurados** sin esquema fijo.
- **Alineación con paradigmas web:** AJAX, APIs REST retornan JSON naturalmente.
- **Object-relational impedance mismatch:** los objetos en código (Python, Java) no mapean limpiamente a tablas relacionales.

### Ventajas y Limitaciones

| Ventajas | Limitaciones |
|---|---|
| Esquema flexible (schema-less) | Menor soporte para relaciones complejas |
| Escalabilidad horizontal | Posibles inconsistencias por redundancia |
| Buen rendimiento en lecturas específicas (un documento = todos sus datos) | Consultas globales pueden ser más costosas |
| Modelo de datos intuitivo para desarrolladores | Riesgo de documentos gigantes |

---

## 2. XML vs. JSON

### XML (eXtensible Markup Language)
Las primeras bases de datos documentales usaron XML. Permite separar datos de formato.

**Tipos:**
- **BD XML "habilitada":** XML almacenado en campo CLOB o tablas. Ejemplos: IBM DB2, PostgreSQL, Oracle, MS SQL Server.
- **BD XML nativa:** la unidad básica es un documento XML. Ejemplos: Sedna, eXist, MarkLogic.

**Desventajas de XML:**
- Mayor espacio por los tags repetitivos.
- Computacionalmente caro de parsear.

### JSON (JavaScript Object Notation)
Surgió como alternativa más ligera a XML. Formato de texto basado en la sintaxis de objeto de JavaScript.

**Ventajas sobre XML:** más compacto, más fácil de parsear, nativo en ecosistemas web.

---

## 3. Jerarquía de Almacenamiento JSON/MongoDB

```
Base de Datos
  └── Colección (≈ tabla relacional, sin esquema fijo)
        └── Documento (≈ fila, unidad básica de almacenamiento)
              └── Pares clave-valor
              └── Documentos anidados
              └── Arreglos (que pueden contener documentos)
```

**Ejemplo de documento JSON:**
```json
{
    "nombre": "José Luis",
    "email": "joseluis.martilara@gmail.com",
    "direccion": {
        "ciudad": "Santiago",
        "pais": "Chile"
    },
    "telefonos": [
        { "tipo": "personal", "numero": "+56912345678" },
        { "tipo": "trabajo",  "numero": "+56223456789" }
    ]
}
```

> **Nota:** `direccion` es un **documento anidado**. `telefonos` es un **arreglo** de documentos anidados.

---

## 4. Anidamiento vs. Referenciación

Este es el **dilema de diseño central** en bases de datos documentales.

### Anidamiento (Embedding)
Los datos relacionados se incluyen **dentro del mismo documento**.

```json
{
    "cliente": "Juan",
    "pedidos": {
        "_id": 123,
        "fecha": "2026-05-01",
        "total": 800
    }
}
```

✅ **Cuándo usar:** datos que siempre se leen juntos, relaciones 1:1 o 1:pocos, jerarquías propietario-contenido.  
❌ **Cuándo evitar:** cuando los datos anidados crecen sin límite (documentos gigantes), o cuando los datos anidados se consultan de forma independiente.

### Referenciación (Referencing)
Los datos relacionados se almacenan en **documentos separados**, vinculados por ID.

```json
// Documento de pedido
{ "_id": 123, "fecha": "2026-05-01", "total": 800 }

// Documento de cliente (referencia)
{ "cliente": "Juan", "pedido_id": 123 }
```

✅ **Cuándo usar:** relaciones M:N, datos que se actualizan independientemente, relaciones que pueden crecer sin límite.  
❌ **Cuándo evitar:** cuando requiere múltiples queries para obtener datos que siempre se necesitan juntos.

---

## 5. Errores Comunes en el Diseño Documental

### Error 1: Pensar en tablas (mapeo 1:1 del modelo relacional)

**Mal diseño (imitando tablas relacionales):**
```json
Usuarios: { "_id": "U1", "nombre": "Juan Pérez" }
Productos: { "_id": "P1", "nombre": "Laptop", "precio": 800 }
Pedidos: { "_id": "O1001", "usuario_id": "U1" }
Items: { "_id": "OI1", "pedido_id": "O1001", "producto_id": "P1", "cantidad": 1 }
```
Este diseño obliga a múltiples consultas para obtener un pedido completo.

**Buen diseño (pensando en cómo se lee la información):**
```json
{
    "_id": "O1001",
    "fecha": "2026-05-04",
    "cliente": { "id": "U1", "nombre": "Juan Pérez" },
    "items": [
        { "producto_id": "P1", "nombre": "Laptop", "precio": 800, "cantidad": 1 }
    ]
}
```

### Error 2: No diseñar en base a las consultas
Si el modelo no considera los patrones de acceso, el rendimiento sufrirá.

**Ejemplo problemático:**
```json
// Post con comentarios embebidos — puede crecer indefinidamente
{
    "_id": "P1",
    "titulo": "Bases de datos NoSQL",
    "comentarios": [
        { "usuario": "Juan", "texto": "Muy buen post", "fecha": "2026-05-01" },
        { "usuario": "Ana",  "texto": "Excelente",     "fecha": "2026-05-02" }
        // ... cientos o miles de comentarios
    ]
}
```

**Problema:** consultas como "comentarios recientes de todos los posts" o "moderar comentarios por usuario" son ineficientes.  
**Solución:** separar comentarios en su propia colección, con referencia al `post_id`.

### Error 3: Documentos gigantes
- **Límite de MongoDB:** 16 MB por documento.
- Genera lecturas ineficientes, escrituras costosas, problemas de concurrencia.

---

## 6. Indexación en MongoDB

Sin índice, MongoDB debe escanear **todos los documentos** de la colección para encontrar los que coincidan (full collection scan).

```json
// Colección con miles de documentos como este:
{ "items": [{ "producto_id": "P1" }] }
```

**Sin índice:** revisar todos los documentos → lento con muchos datos.

**Con índice:**
```javascript
// Crear índice en campo anidado
db.pedidos.createIndex({ "items.producto_id": 1 })
```
El motor usa una estructura de árbol B+ para encontrar documentos en O(log n).

---

## 7. `$lookup`: JOINs en MongoDB

MongoDB soporta algo similar a JOINs con el operador de agregación `$lookup`:

```javascript
// Consulta: pedidos con datos del usuario
db.pedidos.aggregate([
    {
        $lookup: {
            from:         "usuarios",    // colección a unir
            localField:   "usuario_id",  // campo local
            foreignField: "_id",         // campo foráneo
            as:           "usuario"      // nombre del campo resultado
        }
    }
]);

// Resultado:
{ "_id": "O1", "usuario_id": "U1", "total": 100,
  "usuario": [{ "_id": "U1", "nombre": "Juan" }] }
```

**Con `$unwind` para "aplanar" el arreglo resultado:**
```javascript
db.pedidos.aggregate([
    { $lookup: { from: "usuarios", localField: "usuario_id", foreignField: "_id", as: "usuario" } },
    { $unwind: "$usuario" }  // convierte el arreglo en un objeto plano
]);

// Resultado:
{ "_id": "O1", "usuario_id": "U1", "total": 100,
  "usuario": { "_id": "U1", "nombre": "Juan" } }
```

> **Nota profesional:** `$lookup` es más costoso que un JOIN en RDBMS porque opera sobre datos no necesariamente co-localizados. Para consultas frecuentes, se prefiere el anidamiento (embedding) sobre la referenciación.

---

## 8. Caso de Estudio: MongoDB

- **Lanzado en 2009** como producto open source.
- **Formato interno:** BSON (Binary JSON) — menor overhead de parsing, soporte más rico de tipos (fechas, binarios, etc.).
- **MQL (MongoDB Query Language):** inspirado en JSON, permite consultas, agregaciones y actualizaciones complejas.

### Comparación MongoDB vs. Relacional

| Concepto SQL | Concepto MongoDB |
|---|---|
| Base de datos | Base de datos |
| Tabla | Colección |
| Fila / Registro | Documento (JSON/BSON) |
| Columna | Campo |
| INDEX | Index |
| JOIN | $lookup (agregación) |
| FOREIGN KEY | Referencia manual (sin enforcement) |
| GROUP BY | $group (aggregation pipeline) |
| WHERE | $match |
| SELECT | $project |

### Resumen del Modelado Documental
> **"Para modelar una base de datos documental, no se modelan datos, sino cómo se quieren consultarlos."**

Este principio cambia completamente el paradigma: el esquema surge de los patrones de acceso, no de las reglas de normalización.

---

# CLASE 5 — Bases de Datos de Grafos (Neo4j)

## 1. Motivación: ¿Cuándo una BD Relacional o NoSQL Clásica No es Suficiente?

**Casos que motivan las BDs de Grafos:**

- ¿Cómo LinkedIn o Facebook encuentran **contactos de segundo nivel** (amigos de amigos)?
- ¿Cómo Netflix **recomienda contenido** basándose en patrones de usuarios similares?
- ¿Cuál es la **ruta más corta** entre dos ciudades en una red de transporte?

**El problema con las alternativas:**
- **BD Relacional:** puede modelar redes con claves foráneas y auto-joins, pero sufre de problemas de rendimiento en consultas profundas (muchos niveles de conexión). SQL no provee sintaxis nativa para recorridos de grafos.
- **BD Clave-Valor o Documental:** las relaciones entre objetos no son soportadas de forma inherente.

---

## 2. Teoría de Grafos: Conceptos Fundamentales

Un **grafo** es una estructura de datos compuesta por:
- **Nodos (vértices):** representan entidades (personas, productos, lugares).
- **Aristas (enlaces/edges):** representan relaciones entre nodos.

Permite modelar relaciones, caminos y conexiones de forma visual y lógica.

### Aplicaciones de Grafos

| Dominio | Aplicación |
|---|---|
| Ciencias de la computación | Búsqueda de rutas óptimas (Dijkstra, A*) |
| Redes sociales | Análisis de patrones de comportamiento, comunidades |
| Biología y química | Estructuras moleculares, redes neuronales, cadenas alimenticias |
| Logística y transporte | Gestión de tráfico, rutas de entrega |
| Seguridad | Detección de fraude (conexiones sospechosas) |
| Recomendaciones | Filtrado colaborativo basado en grafos |

---

## 3. Bases de Datos de Grafos: Concepto

Todas las bases de datos almacenan **"cosas"**, pero las BDs de grafos reconocen que a veces las **relaciones entre las cosas** son más importantes que las cosas mismas.

**Ejemplo:** en una red social, no solo importa quién es cada usuario, sino **quién conoce a quién**, **quién le gusta a quién** y **qué comunidades se forman**.

### Ventajas y Limitaciones

| Ventajas | Limitaciones |
|---|---|
| Modelan relaciones de forma natural (nodos y aristas) | No eficientes para datos tabulares simples |
| Esquema flexible | Escalabilidad horizontal más compleja |
| Alto rendimiento en consultas de relaciones complejas | Menor estandarización (no hay "SQL universal") |
| Permiten consultas profundas (múltiples niveles de conexión) | No siempre óptimas para agregaciones masivas |

---

## 4. Modelos de Implementación

### RDF (Resource Description Framework)
- Estándar web desarrollado a finales de los años 90.
- Objetivo: modelar recursos web y las relaciones entre ellos.
- Un grafo RDF puede almacenarse en múltiples formatos: XML, tablas relacionales (triplestores), etc.
- Estructura: **triples** (sujeto, predicado, objeto) → `Juan CONOCE Ana`.

### Grafo de Propiedades (Property Graph)
- Modelo RDF enriquecido que permite asociar **atributos tanto a nodos como a aristas**.
- Es la base del modelo de Neo4j.

```
(Juan: Persona {edad: 30}) -[:CONOCE {desde: "2020"}]-> (Ana: Persona {ciudad: "Santiago"})
```

Aquí:
- `Juan` y `Ana` son **nodos** con la etiqueta `Persona` y propiedades.
- `CONOCE` es la **arista** con su propia propiedad `desde`.

---

## 5. Caso de Estudio: Neo4j

- Implementado en **Java**.
- Soporta billones de nodos.
- Propiedades **ACID** completas (a diferencia de muchos NoSQL).
- **Consistencia multiversiones (MVCC)**.
- El referente absoluto del mercado en BDs de grafos.

### Cypher: El Lenguaje de Consulta de Neo4j

Cypher es un lenguaje declarativo similar en espíritu a SQL, pero diseñado para grafos. Usa una sintaxis visual que imita la estructura del grafo.

**Sintaxis básica:**
- `(n:Etiqueta {propiedad: valor})` → nodo
- `-[:TIPO_RELACION]->` → arista dirigida
- `MATCH` → patrón a buscar (equivalente a SELECT/FROM/JOIN en SQL)
- `RETURN` → qué retornar

**Ejemplo 1: Crear nodos y relaciones**
```cypher
// Crear nodos
CREATE (a:Persona {nombre: "Juan"})
CREATE (b:Persona {nombre: "Ana"})

// Crear relación (arista)
CREATE (a)-[:CONOCE]->(b)
```

**Ejemplo 2: Consultar**
```cypher
// Encontrar personas que se conocen entre sí
MATCH (a:Persona)-[:CONOCE]->(b)
RETURN a, b
```

**Ejemplo 3: Consulta profunda (contactos de segundo nivel)**
```cypher
// ¿A quién conoce un conocido de Juan? (nivel 2)
MATCH (a:Persona)-[:CONOCE]->(:Persona)-[:CONOCE]->(c)
WHERE a.nombre = "Juan"
RETURN c
```

> Esta consulta, que en SQL requeriría un auto-join doble y sería costosa a medida que la red crece, en Cypher es trivial y eficiente gracias a la estructura nativa de grafo.

### Gremlin: El Lenguaje Alternativo
- Lenguaje de consulta alternativo para BDs de grafos.
- Orientación **procedural** (describe cómo recorrer el grafo paso a paso).
- Versus Cypher que es **declarativo** (describe qué patrón encontrar).
- Compatible con varias BDs: Amazon Neptune, JanusGraph, etc.

---

## 6. Comparativa Final: ¿Cuándo Usar Cada Tipo de BD?

| Criterio | Relacional (SQL) | Clave-Valor | Wide Column | Documental | Grafos |
|---|---|---|---|---|---|
| **Esquema** | Rígido | Sin esquema | Flexible por fila | Flexible por doc. | Flexible |
| **Relaciones** | Excelente (FK, JOIN) | No soportadas | Sin JOINs | Limitadas ($lookup) | Nativas y eficientes |
| **Escalabilidad** | Vertical (difícil horizontal) | Horizontal | Horizontal | Horizontal | Moderada |
| **Consistencia** | ACID fuerte | Eventual | Sintonizable | Variable | ACID (Neo4j) |
| **Consultas complejas** | SQL completo | Solo por clave | Limitado | Aggregation pipeline | Traversals profundos |
| **Caso de uso ideal** | Transaccional, datos estructurados | Caché, sesiones | Series temporales, logs | APIs, catálogos, CMS | Redes sociales, recomendaciones |
| **Ejemplos** | PostgreSQL, MySQL | Redis, DynamoDB | Cassandra, HBase | MongoDB, CouchBase | Neo4j, Amazon Neptune |

---

## 7. Resumen Integrador: El Continuum del Diseño

El módulo presenta un viaje desde la **teoría pura del dato** hasta la **implementación práctica** en distintos paradigmas:

```
Mundo Real
    ↓
Abstracción Conceptual (Entidades, Relaciones, Semánticas)
    ↓
Modelo Lógico (Relacional, Documental, Grafos, etc.)
    ↓
Modelo Físico (DDL, índices, particiones, réplicas)
    ↓
Sistema en Producción
```

**Principios que trascienden el paradigma:**
1. **El diseño sigue a los datos y las consultas**, no al revés.
2. **No existe la solución universal:** cada paradigma tiene su dominio de excelencia.
3. **Los trade-offs son inevitables:** consistencia vs. disponibilidad, normalización vs. rendimiento, flexibilidad vs. integridad.
4. **La desnormalización es una herramienta, no un error**, cuando se aplica conscientemente.
5. **La indexación es crítica** en cualquier paradigma para rendimiento en lectura.

---

## Bibliografía Utilizada en el Módulo

- Harrison, G. (2015). *Next Generation Databases*. Apress, 1st edition.
- Davoudian, A., Chen, L., Liu, M. (2018). A Survey on NoSQL Stores. *ACM Computing Surveys*, vol. 51, No. 2, pp. 1-40.
- https://cassandra.apache.org/doc/latest/
- https://docs.mongodb.com/manual/
- https://neo4j.com/docs/
- https://db-engines.com/en/ (ranking de popularidad de motores de BD)
- https://blog.bytebytego.com/p/sql-vs-nosql-choosing-the-right-database
