from pyspark.sql import SparkSession
from Extract.Uber_Data_Analytics_Dashboard_Extract import uberExtractor
from Transform.Uber_Data_Analytics_Dashboard_Transform import uberTransformer
from Load.Uber_Data_Analytics_Dashboard_Load import uberLoader
from Config import config  # Importa el archivo de configuración desde la carpeta Config

def main():
    # Inicializar SparkSession
    spark = SparkSession.builder \
        .appName("UberDataAnalyticsPipeline") \
        .config("spark.sql.adaptive.enabled", "true") \
        .config("spark.sql.adaptive.coalescePartitions.enabled", "true") \
        .config("spark.serializer", "org.apache.spark.serializer.KryoSerializer") \
        .getOrCreate()
    
    try:
        # Usar las variables de configuración para las rutas
        input_file = config.input_file
        output_file = config.output_file

        print("Iniciando pipeline ETL con PySpark...")
        
        # Extract - extraer y limpiar datos con PySpark
        print("Fase Extract: Cargando y limpiando datos...")
        extractor = uberExtractor(input_file, output_file)
        spark_data = extractor.queries()  # Retorna un DataFrame de Spark
        
        print(f"Datos extraídos: {spark_data.count()} registros")
        
        # Transform - transformaciones adicionales (opcional, ya que Extract hace la limpieza)
        print("Fase Transform: Aplicando transformaciones adicionales...")
        transformer = uberTransformer(spark_data)
        transformed_data = transformer.transform_data()
        
        print("Datos transformados exitosamente")
        
        # Load - cargar datos en múltiples destinos
        print("Fase Load: Guardando datos...")
        loader = uberLoader(transformed_data, output_file)
        
        # Guardar en CSV
        loader.load_data()
        
        # Guardar en SQLite
        loader.to_sqlite("Extract/files/uber_data.db")
        
        # Opcional: Guardar en Parquet para mejor rendimiento
        loader.to_parquet("Extract/files/uber_data_parquet")
        
        # Mostrar estadísticas finales
        print("\n=== Estadísticas Finales ===")
        loader.show_statistics()
        
        print("\n🎉 ETL proceso completado exitosamente con PySpark!")
        
        # Cerrar la sesión de Spark del extractor
        extractor.close_spark()
        
    except Exception as e:
        print(f"❌ Error en el pipeline ETL: {e}")
        raise
    finally:
        # Cerrar SparkSession
        spark.stop()
        print("SparkSession cerrada correctamente")

if __name__ == "__main__":
    main()
