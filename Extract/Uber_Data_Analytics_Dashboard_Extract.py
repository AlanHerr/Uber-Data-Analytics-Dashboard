import requests  # Importa la librería 'requests' para hacer peticiones HTTP
from pyspark.sql import SparkSession  # Importa SparkSession para trabajar con DataFrames de Spark
from pyspark.sql.functions import col, to_timestamp, regexp_replace, when, isnan, isnull, concat_ws, trim, try_to_timestamp, lit
from pyspark.sql.types import StringType, DoubleType, BooleanType, TimestampType
import pyspark.sql.functions as F 

class uberExtractor:
    def __init__(self, csv_path: str, output_path: str):  
        # Constructor de la clase 'uberExtractor', recibe dos parámetros:
        # - 'csv_path': la ruta del archivo CSV original que se desea cargar
        # - 'output_path': la ruta donde se guardará el archivo CSV limpio después de procesarlo
        
        self.csv = csv_path  # Almacena la ruta del archivo CSV original
        self.output_path = output_path  # Almacena la ruta de salida del archivo limpio
        self.data = None  # Inicializa el atributo 'data', que almacenará los datos del DataFrame de Spark
        self.spark = SparkSession.builder \
            .appName("UberDataAnalytics") \
            .config("spark.sql.adaptive.enabled", "true") \
            .config("spark.sql.adaptive.coalescePartitions.enabled", "true") \
            .getOrCreate()

    def remove_quotes_and_spaces(self):
        """
        Elimina las comillas dobles (") y los espacios en blanco al principio y al final
        de las cadenas de texto en las columnas relevantes usando PySpark.
        """
        # Para las columnas 'Booking ID' y 'Customer ID', eliminamos las comillas dobles y los espacios
        self.data = self.data.withColumn("Booking ID", 
                                        trim(regexp_replace(col("Booking ID"), '"', ''))) \
                           .withColumn("Customer ID", 
                                     trim(regexp_replace(col("Customer ID"), '"', '')))

    def queries(self):
        """
        Carga los datos desde un archivo CSV usando PySpark, realiza una limpieza y transformación de los datos
        y luego guarda el DataFrame limpio en un archivo CSV de salida.
        """
        # Cargar los datos desde el archivo CSV usando PySpark
        self.data = self.spark.read.csv(self.csv, header=True, inferSchema=True)

        # Limpiar y transformar las columnas de datos

        # Limpiar la columna 'Date' y convertirla al formato de fecha (timestamp) con manejo de errores
        self.data = self.data.withColumn("Date", try_to_timestamp(col("Date"), lit("yyyy-MM-dd")))

        # Crear una nueva columna 'DateTime' combinando las columnas 'Date' y 'Time' de manera más robusta
        # Usamos try_to_timestamp para manejar errores de parsing
        self.data = self.data.withColumn("DateTime", 
                                       try_to_timestamp(concat_ws(" ", 
                                                               F.date_format(col("Date"), "yyyy-MM-dd"), 
                                                               col("Time")), 
                                                      lit("yyyy-MM-dd HH:mm:ss")))

        # Eliminar filas con valores nulos en la columna 'Booking ID'
        self.data = self.data.filter(col("Booking ID").isNotNull())

        # Rellenar valores nulos en columnas numéricas con 0
        num_cols = ['Avg VTAT', 'Avg CTAT', 'Booking Value', 'Ride Distance', 'Driver Ratings', 'Customer Rating']
        for column in num_cols:
            if column in self.data.columns:
                # Manejo seguro usando regexp_replace para limpiar "null" strings primero
                self.data = self.data.withColumn(column, 
                                               regexp_replace(col(column), "^null$", "0")) \
                                   .withColumn(column,
                                             when(col(column).isNull(), lit(0.0))
                                             .otherwise(col(column).cast(DoubleType())))

        # Rellenar valores nulos en columnas de texto con 'Unknown'
        text_cols = ['Booking Status', 'Vehicle Type', 'Pickup Location', 'Drop Location',
                     'Reason for cancelling by Customer', 'Driver Cancellation Reason',
                     'Incomplete Rides Reason', 'Payment Method']
        for column in text_cols:
            if column in self.data.columns:
                # Tratamiento seguro para columnas de texto usando regexp_replace
                self.data = self.data.withColumn(column, 
                                               regexp_replace(col(column), "^null$", "Unknown")) \
                                   .withColumn(column,
                                             when(col(column).isNull(), lit("Unknown"))
                                             .otherwise(col(column)))

        # Convertir las columnas de flags (booleanos) a valores booleanos
        flag_cols = ['Cancelled Rides by Customer', 'Cancelled Rides by Driver', 'Incomplete Rides']
        for column in flag_cols:
            if column in self.data.columns:
                # Tratamiento seguro para columnas booleanas usando regexp_replace
                self.data = self.data.withColumn(column, 
                                               regexp_replace(col(column), "^null$", "false")) \
                                   .withColumn(column,
                                             when(col(column).isNull(), lit(False))
                                             .otherwise(col(column).cast(BooleanType())))

        # Eliminar comillas y espacios de las columnas necesarias
        self.remove_quotes_and_spaces()

        # Guardar el DataFrame limpio en un nuevo archivo CSV (solo pandas por ahora para evitar errores de timestamp)
        # self.data.coalesce(1).write.mode("overwrite").option("header", "true").csv(self.output_path.replace('.csv', '_spark'))
        
        # Guardar usando pandas para mayor compatibilidad
        self.data.toPandas().to_csv(self.output_path, index=False)

        return self.data  # Devuelve el DataFrame de Spark limpio

    def response(self):
        """
        Retorna las primeras filas del DataFrame limpio para una vista previa.
        """
        if self.data is None:
            raise ValueError("Los datos no han sido cargados. Llama al método queries() primero.")
        return self.data.show(5)  # Muestra las primeras 5 filas del DataFrame de Spark
    
    def close_spark(self):
        """
        Cierra la sesión de Spark para liberar recursos.
        """
        if self.spark:
            self.spark.stop()
