<<<<<<< HEAD
# Uber Data Analytics Dashboard

## 📖 Descripción del Proyecto

Este proyecto implementa un sistema ETL (Extract, Transform, Load) para el análisis de datos de reservas de Uber en la región NCR (National Capital Region). El sistema procesa datos de viajes, limpia y transforma la información para facilitar el análisis posterior y la creación de dashboards.

## 🎯 Objetivo

El objetivo principal es crear un pipeline de datos robusto que tome datos de reservas de Uber sin procesar y los transforme en un formato limpio y estructurado, listo para análisis y visualización.

## 🏗️ Arquitectura del Proyecto

El proyecto sigue una arquitectura ETL modular organizada en las siguientes capas:

```
📁 Uber-Data-Analytics-Dashboard/
├── 📁 Extract/           # Módulo de extracción y limpieza de datos
├── 📁 Transform/         # Módulo de transformación de datos (en desarrollo)
├── 📁 Load/             # Módulo de carga de datos (en desarrollo)
├── 📁 Config/           # Configuraciones del proyecto
├── 📄 main.py           # Archivo principal de ejecución
├── 📄 requirements.txt  # Dependencias del proyecto
└── 📊 Datasets CSV      # Archivos de datos originales y procesados
=======
# 🚗 Uber Data Analytics Dashboard

## 📖 Descripción del Proyecto

Este proyecto implementa un **pipeline ETL (Extract, Transform, Load)** completo para el análisis de datos de reservas de Uber en la región NCR (National Capital Region). El sistema procesa datos de viajes, limpia y transforma la información para facilitar el análisis posterior y la creación de dashboards analíticos.

## 🎯 Objetivos

- **Procesamiento de datos**: Limpiar y estandarizar datos de reservas de Uber
- **Pipeline ETL**: Implementar una arquitectura modular y escalable
- **Múltiples formatos**: Generar salidas en CSV y SQLite
- **Calidad de datos**: Garantizar integridad y consistencia de la información
- **Análisis preparado**: Datos listos para visualización y análisis avanzado

## 🏗️ Arquitectura del Proyecto

```
📁 Uber-Data-Analytics-Dashboard/
├── 📁 Config/                    # Configuraciones centralizadas
│   ├── __init__.py              # Inicializador del paquete
│   └── config.py                # Variables de configuración
├── 📁 Extract/                  # Módulo de extracción de datos
│   ├── files/                   # Archivos de datos
│   │   ├── ncr_ride_bookings.csv          # Dataset original
│   │   ├── ncr_ride_bookings_cleaned.csv  # Dataset procesado
│   │   └── uber_data.db                   # Base de datos SQLite
│   └── Uber_Data_Analytics_Dashboard_Extract.py
├── 📁 Transform/                # Módulo de transformación
│   └── Uber_Data_Analytics_Dashboard_Transform.py
├── 📁 Load/                     # Módulo de carga
│   └── Uber_Data_Analytics_Dashboard_Load.py
├── 📄 main.py                   # Archivo principal de ejecución
├── 📄 requirements.txt          # Dependencias del proyecto
├── 📄 README.md                 # Documentación
└── 📄 .gitignore               # Archivos excluidos de Git
>>>>>>> Release
```

## 🛠️ Tecnologías Utilizadas

<<<<<<< HEAD
- **Python 3.x**: Lenguaje principal de desarrollo
- **Pandas**: Manipulación y análisis de datos
- **NumPy**: Cálculos numéricos y manejo de arrays
- **Requests**: Peticiones HTTP (preparado para futuras integraciones)

## 📊 Conjunto de Datos

### Datos de Entrada (`ncr_ride_bookings.csv`)
Contiene información de reservas de Uber con las siguientes columnas:
- **Date**: Fecha de la reserva
- **Time**: Hora de la reserva
- **Booking ID**: Identificador único de la reserva
- **Booking Status**: Estado de la reserva (Completed, Incomplete, No Driver Found, etc.)
- **Customer ID**: Identificador del cliente
- **Vehicle Type**: Tipo de vehículo (Auto, Go Sedan, Premier Sedan, eBike)
- **Pickup Location**: Ubicación de recogida
- **Drop Location**: Ubicación de destino
- **Avg VTAT**: Tiempo promedio de llegada del vehículo
- **Avg CTAT**: Tiempo promedio de llegada del cliente
- **Booking Value**: Valor de la reserva
- **Ride Distance**: Distancia del viaje
- **Driver Ratings**: Calificación del conductor
- **Customer Rating**: Calificación del cliente
- **Payment Method**: Método de pago
- **Campos de cancelación**: Información sobre cancelaciones y razones

### Datos de Salida (`ncr_ride_bookings_cleaned.csv`)
Dataset procesado y limpio con las siguientes mejoras:
- Eliminación de comillas y espacios innecesarios
- Conversión de tipos de datos apropiados
- Manejo de valores nulos
- Nueva columna **DateTime** (combinación de Date y Time)
- Normalización de valores booleanos

## 🔧 Funcionalidades Implementadas

### Módulo Extract (`uberExtractor`)

La clase `uberExtractor` implementa las siguientes funcionalidades:

#### 1. **Limpieza de Datos**
- Eliminación de comillas dobles en IDs
- Eliminación de espacios en blanco innecesarios
- Conversión de tipos de datos apropiados

#### 2. **Transformación de Fechas y Horas**
- Conversión de columnas Date a formato datetime
- Conversión de columnas Time a formato time
- Creación de columna DateTime combinada

#### 3. **Manejo de Valores Nulos**
- **Columnas numéricas**: Rellenado con 0
- **Columnas de texto**: Rellenado con 'Unknown'
- **Eliminación de filas** con Booking ID nulo

#### 4. **Normalización de Tipos de Datos**
- Conversión de flags booleanos
- Normalización de columnas numéricas
- Estandarización de columnas de texto
=======
| Tecnología | Versión | Propósito |
|------------|---------|-----------|
| **Python** | 3.12+ | Lenguaje principal |
| **Pandas** | 2.3.2 | Manipulación y análisis de datos |
| **NumPy** | 2.3.2 | Cálculos numéricos |
| **SQLite3** | Built-in | Base de datos local |
| **Requests** | Latest | Peticiones HTTP (futuras integraciones) |

## 📊 Estructura de Datos

### Dataset de Entrada (`ncr_ride_bookings.csv`)

**Información de reservas de Uber con 21 columnas:**

| Columna | Tipo | Descripción |
|---------|------|-------------|
| `Date` | Date | Fecha de la reserva |
| `Time` | Time | Hora de la reserva |
| `Booking ID` | String | Identificador único de reserva |
| `Booking Status` | String | Estado (Completed, Incomplete, No Driver Found, etc.) |
| `Customer ID` | String | Identificador del cliente |
| `Vehicle Type` | String | Tipo de vehículo (Auto, Go Sedan, Premier Sedan, eBike) |
| `Pickup Location` | String | Ubicación de recogida |
| `Drop Location` | String | Ubicación de destino |
| `Avg VTAT` | Float | Tiempo promedio de llegada del vehículo |
| `Avg CTAT` | Float | Tiempo promedio de llegada del cliente |
| `Booking Value` | Float | Valor monetario de la reserva |
| `Ride Distance` | Float | Distancia del viaje en km |
| `Driver Ratings` | Float | Calificación del conductor (1-5) |
| `Customer Rating` | Float | Calificación del cliente (1-5) |
| `Payment Method` | String | Método de pago utilizado |
| `Cancelled Rides by Customer` | Boolean | Cancelación por cliente |
| `Cancelled Rides by Driver` | Boolean | Cancelación por conductor |
| `Incomplete Rides` | Boolean | Viajes incompletos |
| `Reason for cancelling by Customer` | String | Motivo de cancelación del cliente |
| `Driver Cancellation Reason` | String | Motivo de cancelación del conductor |
| `Incomplete Rides Reason` | String | Motivo de viaje incompleto |

### Dataset de Salida (`ncr_ride_bookings_cleaned.csv`)

**Dataset procesado con mejoras:**
- ✅ **Nueva columna `DateTime`**: Combinación de Date + Time
- ✅ **IDs limpios**: Sin comillas ni espacios extraños
- ✅ **Valores nulos manejados**: Estrategias diferenciadas por tipo
- ✅ **Tipos de datos correctos**: Fechas, números y booleanos normalizados
- ✅ **Consistencia**: Datos estandarizados para análisis

## 🔧 Funcionalidades del Pipeline ETL

### 🔍 Extract (`uberExtractor`)

**Responsabilidades:**
- Carga de datos desde CSV
- Validación inicial de estructura
- Limpieza básica de formato

**Métodos principales:**
- `__init__(csv_path, output_path)`: Inicialización con rutas
- `queries()`: Proceso completo de extracción y limpieza
- `remove_quotes_and_spaces()`: Limpieza de caracteres especiales
- `response()`: Vista previa de los datos

### 🔄 Transform (`uberTransformer`)

**Responsabilidades:**
- Transformación de tipos de datos
- Creación de nuevas columnas derivadas
- Normalización de valores

**Procesos de transformación:**
1. **Fechas y horas**: Conversión a datetime y creación de columna combinada
2. **Valores nulos**:
   - Columnas numéricas → 0
   - Columnas de texto → 'Unknown'
   - Eliminación de filas con Booking ID nulo
3. **Tipos de datos**: Normalización de booleanos y numéricos
4. **Limpieza**: Eliminación de comillas y espacios

### 📥 Load (`uberLoader`)

**Responsabilidades:**
- Persistencia de datos procesados
- Múltiples formatos de salida
- Manejo de errores en escritura

**Métodos de carga:**
- `load_data()`: Guardar en CSV
- `to_csv(path)`: Guardar CSV personalizado
- `to_sqlite(db_path, table_name)`: Guardar en SQLite
>>>>>>> Release

## 🚀 Instalación y Uso

### Prerrequisitos
```bash
<<<<<<< HEAD
Python 3.x
pip (gestor de paquetes de Python)
venv (módulo de entornos virtuales - incluido con Python 3.3+)
```

### Instalación
1. Clonar el repositorio:
=======
Python 3.12+
pip (gestor de paquetes)
venv (entornos virtuales)
```

### Instalación Paso a Paso

1. **Clonar el repositorio**:
>>>>>>> Release
```bash
git clone https://github.com/AlanHerr/Uber-Data-Analytics-Dashboard.git
cd Uber-Data-Analytics-Dashboard
```

<<<<<<< HEAD
2. Crear y activar el entorno virtual:
=======
2. **Crear y activar entorno virtual**:
>>>>>>> Release
```bash
# Crear entorno virtual
python -m venv uber_env

# Activar entorno virtual
# En Linux/Mac:
source uber_env/bin/activate
<<<<<<< HEAD

=======
>>>>>>> Release
# En Windows:
uber_env\Scripts\activate
```

<<<<<<< HEAD
3. Instalar dependencias:
=======
3. **Instalar dependencias**:
>>>>>>> Release
```bash
pip install -r requirements.txt
```

### Ejecución
<<<<<<< HEAD
=======

>>>>>>> Release
```bash
python main.py
```

<<<<<<< HEAD
## 📝 Ejemplo de Uso

```python
from Extract.Uber_Data_Analytics_Dashboard_Extract import uberExtractor

# Configurar rutas de archivos
input_file = "ncr_ride_bookings.csv"
output_file = "ncr_ride_bookings_cleaned.csv"

# Crear instancia del extractor
extractor = uberExtractor(input_file, output_file)

# Procesar datos
cleaned_data = extractor.queries()

# Ver muestra de datos limpios
preview = extractor.response()
print(preview.head())
```

## 📈 Resultados del Procesamiento

### Antes del Procesamiento
- Datos con comillas innecesarias: `"CNR5884300"`
- Valores nulos sin manejar
- Fechas y horas separadas
- Tipos de datos inconsistentes

### Después del Procesamiento
- IDs limpios: `CNR5884300`
- Valores nulos manejados apropiadamente
- Columna DateTime unificada
- Tipos de datos consistentes y apropiados

## 📄 Licencia

Este proyecto está bajo la licencia MIT - ver el archivo [LICENSE](LICENSE) para más detalles.

---
*Proyecto desarrollado como parte del análisis de datos de movilidad urbana en la región NCR.*
=======
**Salida esperada:**
```
Datos guardados en la base de datos SQLite: Extract/files/uber_data.db, tabla: ride_bookings
ETL proceso completado exitosamente.
```

## 📝 Configuración

### Archivo `Config/config.py`

```python
# Rutas de archivos
input_file = "Extract/files/ncr_ride_bookings.csv"
output_file = "Extract/files/ncr_ride_bookings_cleaned.csv"

# Configuraciones adicionales pueden agregarse aquí
```


## 📈 Resultados y Métricas

### Antes del Procesamiento
- ❌ Datos con comillas: `"CNR5884300"`
- ❌ Valores nulos sin manejar
- ❌ Fechas y horas separadas
- ❌ Tipos de datos inconsistentes
- ❌ Espacios y caracteres extraños

### Después del Procesamiento
- ✅ IDs limpios: `CNR5884300`
- ✅ Valores nulos manejados estratégicamente
- ✅ Columna DateTime unificada
- ✅ Tipos de datos consistentes
- ✅ Datos listos para análisis

### Archivos Generados

| Archivo | Tamaño | Formato | Propósito |
|---------|--------|---------|-----------|
| `ncr_ride_bookings.csv` | ~25MB | CSV | Dataset original |
| `ncr_ride_bookings_cleaned.csv` | ~28MB | CSV | Dataset procesado |
| `uber_data.db` | ~31MB | SQLite | Base de datos |

### Convenciones de Commits
- `feat:` Nueva funcionalidad
- `fix:` Corrección de bugs
- `docs:` Documentación
- `style:` Formato de código
- `refactor:` Refactorización
- `test:` Tests

## 📄 Licencia

Este proyecto está bajo la licencia MIT. Ver archivo [LICENSE](LICENSE) para más detalles.

## 👨‍💻 Autor

**Alan Herrera** 
- GitHub: [@AlanHerr](https://github.com/AlanHerr)
>>>>>>> Release
