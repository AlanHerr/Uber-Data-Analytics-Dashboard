import requests
import pandas as pd
import numpy as np

class uberExtractor:
    def __init__(self, csv_path: str, output_path: str):  
        self.csv = csv_path
        self.output_path = output_path  # Ruta de salida para el archivo limpio
        self.data = None

    def remove_quotes_and_spaces(self):
        """
        Elimina las comillas y los espacios en blanco de las columnas específicas.
        """
        # Eliminar comillas y espacios en las columnas relevantes
        self.data['Booking ID'] = self.data['Booking ID'].str.strip('"').str.strip()
        self.data['Customer ID'] = self.data['Customer ID'].str.strip('"').str.strip()

    def queries(self):
        """
        Carga los datos desde un archivo CSV y realiza la limpieza y transformación de los datos.
        Luego guarda el DataFrame limpio en un archivo CSV.
        """
        # Cargar los datos
        self.data = pd.read_csv(self.csv)

        # Limpiar y transformación de datos

        # Limpiar la columna 'Date' y convertirla en datetime
        self.data['Date'] = pd.to_datetime(self.data['Date'], errors='coerce')

        # Limpiar la columna 'Time' y convertirla en datetime
        self.data['Time'] = pd.to_datetime(self.data['Time'], format='%H:%M:%S', errors='coerce').dt.time

        # Crear una nueva columna 'DateTime' combinando 'Date' y 'Time'
        self.data['DateTime'] = pd.to_datetime(self.data['Date'].astype(str) + ' ' + self.data['Time'].astype(str), errors='coerce')

        # Eliminar filas con 'Booking ID' nulo
        self.data = self.data.dropna(subset=['Booking ID'])

        # Rellenar valores nulos en columnas numéricas con 0
        num_cols = ['Avg VTAT', 'Avg CTAT', 'Booking Value', 'Ride Distance', 'Driver Ratings', 'Customer Rating']
        for col in num_cols:
            if col in self.data.columns:
                self.data[col] = pd.to_numeric(self.data[col], errors='coerce').fillna(0)

        # Rellenar valores nulos en columnas de texto con 'Unknown'
        text_cols = ['Booking Status', 'Vehicle Type', 'Pickup Location', 'Drop Location',
                     'Reason for cancelling by Customer', 'Driver Cancellation Reason',
                     'Incomplete Rides Reason', 'Payment Method']
        for col in text_cols:
            if col in self.data.columns:
                self.data[col] = self.data[col].fillna('Unknown')

        # Convertir las columnas de flags a booleanos
        flag_cols = ['Cancelled Rides by Customer', 'Cancelled Rides by Driver', 'Incomplete Rides']
        for col in flag_cols:
            if col in self.data.columns:
                self.data[col] = self.data[col].astype(bool)

        # Eliminar comillas y espacios en las columnas necesarias
        self.remove_quotes_and_spaces()

        # Guardar el DataFrame limpio en un nuevo archivo CSV
        self.data.to_csv(self.output_path, index=False)
        
        return self.data

    def response(self):
        if self.data is None:
            raise ValueError("Los datos no han sido cargados. Llama al método queries() primero.")
        return self.data.head()
