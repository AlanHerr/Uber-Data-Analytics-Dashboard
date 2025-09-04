from Extract.Uber_Data_Analytics_Dashboard_Extract import uberExtractor
from Transform.Uber_Data_Analytics_Dashboard_Transform import uberTransformer
from Load.Uber_Data_Analytics_Dashboard_Load import uberLoader
from Config import config  # Importa el archivo de configuración desde la carpeta Config

# Usar las variables de configuración para las rutas
input_file = config.input_file
output_file = config.output_file

# Extract - usar la versión original del extractor
extractor = uberExtractor(input_file, output_file)
data = extractor.queries()  # Este método ya limpia y retorna los datos

# Load - guardar también en SQLite
loader = uberLoader(data, output_file)
loader.to_sqlite("Extract/files/uber_data.db")  # Guardar en SQLite en la ruta correcta

print("ETL proceso completado exitosamente.")
