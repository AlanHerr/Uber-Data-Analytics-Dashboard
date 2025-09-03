import pandas as pd

class uberExtractor:
    def __init__(self, csv_path: str):
        self.csv = csv_path
        self.data = None

    def extract_data(self):
        """
        Extrae los datos desde el archivo CSV.
        """
        self.data = pd.read_csv(self.csv)
        return self.data
