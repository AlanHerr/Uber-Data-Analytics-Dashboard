import requests  # Importa la librería 'requests' para hacer peticiones HTTP (aunque no se usa en este código, es posible que sea parte del proyecto más grande)
import pandas as pd  # Importa pandas, una librería potente para manipulación y análisis de datos en Python
import numpy as np  # Importa numpy, una librería para manejar arrays y funciones matemáticas (aunque no se usa explícitamente aquí)

class uberExtractor:
    def __init__(self, csv_path: str, output_path: str):  
        # Constructor de la clase 'uberExtractor', recibe dos parámetros:
        # - 'csv_path': la ruta del archivo CSV original que se desea cargar
        # - 'output_path': la ruta donde se guardará el archivo CSV limpio después de procesarlo
        
        self.csv = csv_path  # Almacena la ruta del archivo CSV original
        self.output_path = output_path  # Almacena la ruta de salida del archivo limpio
        self.data = None  # Inicializa el atributo 'data', que almacenará los datos del archivo CSV

    def remove_quotes_and_spaces(self):
        """
        Elimina las comillas dobles (") y los espacios en blanco al principio y al final
        de las cadenas de texto en las columnas relevantes.
        """
        # Para las columnas 'Booking ID' y 'Customer ID', eliminamos las comillas dobles y los espacios
        self.data['Booking ID'] = self.data['Booking ID'].str.strip('"').str.strip()  # Elimina comillas y espacios de 'Booking ID'
        self.data['Customer ID'] = self.data['Customer ID'].str.strip('"').str.strip()  # Elimina comillas y espacios de 'Customer ID'

    def queries(self):
        """
        Carga los datos desde un archivo CSV, realiza una limpieza y transformación de los datos
        y luego guarda el DataFrame limpio en un archivo CSV de salida.
        """
        # Cargar los datos desde el archivo CSV
        self.data = pd.read_csv(self.csv)  # Usa pandas para leer el archivo CSV y cargarlo en el DataFrame 'self.data'

        # Limpiar y transformar las columnas de datos

        # Limpiar la columna 'Date' y convertirla al formato de fecha (datetime)
        self.data['Date'] = pd.to_datetime(self.data['Date'], errors='coerce')  # Convierte 'Date' a formato datetime, usa 'coerce' para manejar valores inválidos

        # Limpiar la columna 'Time' y convertirla al formato de hora (time)
        self.data['Time'] = pd.to_datetime(self.data['Time'], format='%H:%M:%S', errors='coerce').dt.time  # Convierte 'Time' a formato hora

        # Crear una nueva columna 'DateTime' combinando las columnas 'Date' y 'Time' para crear un valor completo de fecha y hora
        self.data['DateTime'] = pd.to_datetime(self.data['Date'].astype(str) + ' ' + self.data['Time'].astype(str), errors='coerce')  # Combina 'Date' y 'Time' en una nueva columna 'DateTime'

        # Eliminar filas con valores nulos en la columna 'Booking ID'
        self.data = self.data.dropna(subset=['Booking ID'])  # Elimina filas que tienen 'Booking ID' como NaN (vacío)

        # Rellenar valores nulos en columnas numéricas con 0
        num_cols = ['Avg VTAT', 'Avg CTAT', 'Booking Value', 'Ride Distance', 'Driver Ratings', 'Customer Rating']  # Definir las columnas numéricas
        for col in num_cols:  # Iterar sobre cada columna numérica
            if col in self.data.columns:  # Si la columna existe en el DataFrame
                self.data[col] = pd.to_numeric(self.data[col], errors='coerce').fillna(0)  # Convierte a numérico y reemplaza NaN con 0

        # Rellenar valores nulos en columnas de texto con 'Unknown'
        text_cols = ['Booking Status', 'Vehicle Type', 'Pickup Location', 'Drop Location',
                     'Reason for cancelling by Customer', 'Driver Cancellation Reason',
                     'Incomplete Rides Reason', 'Payment Method']  # Definir las columnas de texto
        for col in text_cols:  # Iterar sobre cada columna de texto
            if col in self.data.columns:  # Si la columna existe en el DataFrame
                self.data[col] = self.data[col].fillna('Unknown')  # Rellenar valores NaN con 'Unknown'

        # Convertir las columnas de flags (booleanos) a valores booleanos
        flag_cols = ['Cancelled Rides by Customer', 'Cancelled Rides by Driver', 'Incomplete Rides']  # Definir las columnas de flags
        for col in flag_cols:  # Iterar sobre cada columna de flags
            if col in self.data.columns:  # Si la columna existe en el DataFrame
                self.data[col] = self.data[col].astype(bool)  # Convertir la columna a tipo booleano

        # Eliminar comillas y espacios de las columnas necesarias (como 'Booking ID' y 'Customer ID')
        self.remove_quotes_and_spaces()  # Llamamos a la función que limpia comillas y espacios en las columnas relevantes

        # Guardar el DataFrame limpio en un nuevo archivo CSV
        self.data.to_csv(self.output_path, index=False)  # Guarda los datos limpios en el archivo de salida, sin los índices

        return self.data  # Devuelve el DataFrame limpio

    def response(self):
        """
        Retorna las primeras filas del DataFrame limpio para una vista previa.
        """
        if self.data is None:  # Si no se ha cargado ningún dato
            raise ValueError("Los datos no han sido cargados. Llama al método queries() primero.")  # Lanza un error si no hay datos
        return self.data.head()  # Retorna las primeras filas del DataFrame limpio
