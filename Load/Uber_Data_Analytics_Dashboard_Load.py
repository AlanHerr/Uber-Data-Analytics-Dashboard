
from pyspark.sql import SparkSession, DataFrame
import sqlite3

class uberLoader:
    """
    Clase para cargar los datos limpios a un destino usando PySpark.
    """
    def __init__(self, df: DataFrame, output_path: str):
        self.df = df
        self.output_path = output_path
        # Usar la sesión de Spark existente o crear una nueva si no existe
        self.spark = SparkSession.getActiveSession()
        if self.spark is None:
            self.spark = SparkSession.builder \
                .appName("UberDataLoader") \
                .config("spark.sql.adaptive.enabled", "true") \
                .config("spark.sql.adaptive.coalescePartitions.enabled", "true") \
                .getOrCreate()

    def load_data(self):
        """
        Guarda el DataFrame de Spark en un archivo CSV usando pandas para mayor compatibilidad.
        """
        try:
            # Guardar usando pandas para mayor compatibilidad con timestamps
            # self.df.coalesce(1).write.mode("overwrite").option("header", "true").csv(self.output_path.replace('.csv', '_spark'))
            
            # Guardar en formato pandas para compatibilidad
            self.df.toPandas().to_csv(self.output_path, index=False)
            
            print(f"El archivo limpio ha sido guardado en: {self.output_path}")
        except Exception as e:
            print(f"Error al guardar datos: {e}")

    def to_csv(self, output_path: str):
        """
        Guarda el DataFrame de Spark en un archivo CSV usando pandas.
        """
        try:
            # Guardar usando pandas para compatibilidad
            # self.df.coalesce(1).write.mode("overwrite").option("header", "true").csv(output_path.replace('.csv', '_spark'))
            
            # Guardar en formato pandas para compatibilidad
            self.df.toPandas().to_csv(output_path, index=False)
            
            print(f"Datos guardados en {output_path}")
        except Exception as e:
            print(f"Error al guardar datos: {e}")

    def to_sqlite(self, db_path="Extract/files/uber_data.db", table_name="ride_bookings"):
        """
        Guarda el DataFrame de Spark en una base de datos SQLite.
        """
        try:
            # Convertir a pandas para guardar en SQLite (PySpark no tiene conector nativo para SQLite)
            pandas_df = self.df.toPandas()
            
            conn = sqlite3.connect(db_path)
            pandas_df.to_sql(table_name, conn, if_exists='replace', index=False)
            conn.close()
            
            print(f"Datos guardados en la base de datos SQLite: {db_path}, tabla: {table_name}")
        except Exception as e:
            print(f"Error al guardar en SQLite: {e}")

    def to_parquet(self, output_path: str):
        """
        Guarda el DataFrame de Spark en formato Parquet (más eficiente para big data).
        """
        try:
            self.df.write.mode("overwrite").parquet(output_path)
            print(f"Datos guardados en formato Parquet en: {output_path}")
        except Exception as e:
            print(f"Error al guardar en Parquet: {e}")

    def to_delta(self, output_path: str):
        """
        Guarda el DataFrame de Spark en formato Delta Lake (requiere delta-spark).
        """
        try:
            self.df.write.format("delta").mode("overwrite").save(output_path)
            print(f"Datos guardados en formato Delta en: {output_path}")
        except Exception as e:
            print(f"Error al guardar en Delta: {e}")
            print("Nota: Asegúrate de tener delta-spark instalado para usar esta funcionalidad")

    def show_statistics(self):
        """
        Muestra estadísticas básicas del DataFrame.
        """
        try:
            print("Estadísticas del DataFrame:")
            self.df.describe().show()
            
            print(f"Número total de registros: {self.df.count()}")
            print(f"Número de columnas: {len(self.df.columns)}")
            
        except Exception as e:
            print(f"Error al mostrar estadísticas: {e}")
