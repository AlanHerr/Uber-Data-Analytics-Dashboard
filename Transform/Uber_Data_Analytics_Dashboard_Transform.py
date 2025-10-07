from pyspark.sql import SparkSession, DataFrame
from pyspark.sql.functions import col, to_timestamp, regexp_replace, when, isnan, isnull, concat_ws, trim, try_to_timestamp, lit
from pyspark.sql.types import StringType, DoubleType, BooleanType, TimestampType
import pyspark.sql.functions as F

class uberTransformer:
    def __init__(self, data: DataFrame):
        self.data = data
        # Usar la sesión de Spark existente o crear una nueva si no existe
        self.spark = SparkSession.getActiveSession()
        if self.spark is None:
            self.spark = SparkSession.builder \
                .appName("UberDataTransformer") \
                .config("spark.sql.adaptive.enabled", "true") \
                .config("spark.sql.adaptive.coalescePartitions.enabled", "true") \
                .getOrCreate()

    def remove_quotes_and_spaces(self):
        """
        Elimina las comillas y los espacios en blanco de las columnas específicas usando PySpark.
        """
        self.data = self.data.withColumn("Booking ID", 
                                        trim(regexp_replace(col("Booking ID"), '"', ''))) \
                           .withColumn("Customer ID", 
                                     trim(regexp_replace(col("Customer ID"), '"', '')))

    def transform_data(self):
        """
        Realiza la limpieza y transformación de los datos usando PySpark.
        """
        # Limpiar la columna 'Date' y convertirla al formato de fecha (timestamp) con manejo de errores
        self.data = self.data.withColumn("Date", try_to_timestamp(col("Date"), lit("yyyy-MM-dd")))

        # Crear una nueva columna 'DateTime' combinando 'Date' y 'Time' con manejo de errores
        self.data = self.data.withColumn("DateTime", 
                                       try_to_timestamp(concat_ws(" ", 
                                                               F.date_format(col("Date"), "yyyy-MM-dd"), 
                                                               col("Time")), 
                                                      lit("yyyy-MM-dd HH:mm:ss")))

        # Eliminar filas con 'Booking ID' nulo
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

        # Convertir las columnas de flags a booleanos
        flag_cols = ['Cancelled Rides by Customer', 'Cancelled Rides by Driver', 'Incomplete Rides']
        for column in flag_cols:
            if column in self.data.columns:
                # Tratamiento seguro para columnas booleanas usando regexp_replace
                self.data = self.data.withColumn(column, 
                                               regexp_replace(col(column), "^null$", "false")) \
                                   .withColumn(column,
                                             when(col(column).isNull(), lit(False))
                                             .otherwise(col(column).cast(BooleanType())))

        # Eliminar comillas y espacios en las columnas necesarias
        self.remove_quotes_and_spaces()

        return self.data

    def get_statistics(self):
        """
        Obtiene estadísticas básicas del DataFrame usando PySpark.
        """
        if self.data is None:
            raise ValueError("Los datos no han sido cargados.")
        
        return self.data.describe()

    def show_sample(self, n=5):
        """
        Muestra una muestra de los datos transformados.
        """
        if self.data is None:
            raise ValueError("Los datos no han sido cargados.")
        
        return self.data.show(n)
