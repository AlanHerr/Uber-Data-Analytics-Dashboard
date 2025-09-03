from Extract.Uber_Data_Analytics_Dashboard_Extract import uberExtractor
from Transform.Uber_Data_Analytics_Dashboard_Transform import uberTransformer
from Load.Uber_Data_Analytics_Dashboard_Load import uberLoader
import config  # Importa el archivo de configuración

# Usar las variables de configuración para las rutas
input_file = config.input_file
output_file = config.output_file

# Extract
extractor = uberExtractor(input_file)
data = extractor.extract_data()

# Transform
transformer = uberTransformer(data)
transformed_data = transformer.transform_data()

# Load
loader = uberLoader(transformed_data, output_file)
loader.load_data()

print("ETL proceso completado exitosamente.")