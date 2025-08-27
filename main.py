from Extract.Uber_Data_Analytics_Dashboard_Extract import uberExtractor

# Ruta del archivo CSV original
input_file = "ncr_ride_bookings.csv"

# Ruta donde se guardará el archivo limpio
output_file = "ncr_ride_bookings_cleaned.csv"

# Crear una instancia de uberExtractor con la ruta de entrada y salida
extractor = uberExtractor(input_file, output_file)

# Llamar al método queries() para cargar, limpiar y guardar los datos
extractor.queries()

# Confirmación de que el archivo limpio se generó
print(f"El archivo limpio ha sido guardado en: {output_file}")
