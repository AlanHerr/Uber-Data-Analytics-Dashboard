import requests
import pandas as pd
import numpy as np


class uberExtractor:
    def __init__(self, csv_path: str):  # <-- corregido aquí
        self.csv = csv_path
        self.data = None

    def queries(self):
        self.data = pd.read_csv(self.csv)
        return self.data

    def response(self):
        if self.data is None:
            raise ValueError("Los datos no han sido cargados. Llama al método queries() primero.")
        return self.data.head()