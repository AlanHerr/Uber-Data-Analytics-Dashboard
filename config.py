# Configuración del proyecto Uber Data Analytics Dashboard

# Rutas de archivos
input_file = "Extract/files/ncr_ride_bookings.csv"
output_file = "Extract/files/ncr_ride_bookings_cleaned.csv"

# Configuraciones de procesamiento
DEFAULT_NUMERIC_FILL = 0
DEFAULT_TEXT_FILL = "Unknown"

# Columnas a procesar
NUMERIC_COLUMNS = [
    'Avg VTAT', 
    'Avg CTAT', 
    'Booking Value', 
    'Ride Distance', 
    'Driver Ratings', 
    'Customer Rating'
]

TEXT_COLUMNS = [
    'Booking Status', 
    'Vehicle Type', 
    'Pickup Location', 
    'Drop Location',
    'Reason for cancelling by Customer', 
    'Driver Cancellation Reason',
    'Incomplete Rides Reason', 
    'Payment Method'
]

FLAG_COLUMNS = [
    'Cancelled Rides by Customer', 
    'Cancelled Rides by Driver', 
    'Incomplete Rides'
]
