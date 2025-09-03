
import pandas as pd
import sqlite3

class uberLoader:
    """
    Clase para cargar los datos limpios a un destino.
    """
    def __init__(self, df, output_path):
        self.df = df
        self.output_path = output_path

    def load_data(self):
        """
        Guarda el DataFrame limpio en un archivo CSV.
        """
        try:
            self.df.to_csv(self.output_path, index=False)
            print(f"El archivo limpio ha sido guardado en: {self.output_path}")
        except Exception as e:
            print(f"Error al guardar datos: {e}")

    def to_csv(self, output_path):
        """
        Guarda el DataFrame limpio en un archivo CSV.
        """
        try:
            self.df.to_csv(output_path, index=False)
            print(f"Datos guardados en {output_path}")
        except Exception as e:
            print(f"Error al guardar datos: {e}")

    def to_sqlite(self, db_path="Extract/files/uber_data.db", table_name="ride_bookings"):
        """
        Guarda el DataFrame limpio en una base de datos SQLite.
        """
        try:
            conn = sqlite3.connect(db_path)
            self.df.to_sql(table_name, conn, if_exists='replace', index=False)
            conn.close()
            print(f"Datos guardados en la base de datos SQLite: {db_path}, tabla: {table_name}")
        except Exception as e:
            print(f"Error al guardar en SQLite: {e}")
