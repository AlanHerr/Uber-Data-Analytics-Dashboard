# Rutas de archivos
input_file = "r/workspaces/Uber-Data-Analytics-Dashboard/Extract/files/ncr_ride_bookings.csv"
output_file = "r/workspaces/Uber-Data-Analytics-Dashboard/Extract/files/ncr_ride_bookings_cleaned.csv"

class Config:
    """
    Clase de configuración para rutas y parámetros del ETL.
    """
    INPUT_PATH = '/workspaces/ETLProject/Extract/Files/ncr_ride_bookings.csv'
    SQLITE_DB_PATH = '/workspaces/ETLProject/Extract/Files/etl_data.db'
    SQLITE_TABLE = 'ride_bookings_clean'