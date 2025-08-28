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
```

## 🛠️ Tecnologías Utilizadas

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

## 🚀 Instalación y Uso

### Prerrequisitos
```bash
Python 3.x
pip (gestor de paquetes de Python)
venv (módulo de entornos virtuales - incluido con Python 3.3+)
```

### Instalación
1. Clonar el repositorio:
```bash
git clone https://github.com/AlanHerr/Uber-Data-Analytics-Dashboard.git
cd Uber-Data-Analytics-Dashboard
```

2. Crear y activar el entorno virtual:
```bash
# Crear entorno virtual
python -m venv uber_env

# Activar entorno virtual
# En Linux/Mac:
source uber_env/bin/activate

# En Windows:
uber_env\Scripts\activate
```

3. Instalar dependencias:
```bash
pip install -r requirements.txt
```

### Ejecución
```bash
python main.py
```

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