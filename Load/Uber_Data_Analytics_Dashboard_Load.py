import pandas as pd

class uberLoader:
    def __init__(self, data: pd.DataFrame, output_path: str):
        self.data = data
        self.output_path = output_path

    def load_data(self):
        """
        Carga los datos transformados en un archivo CSV.
        """
        self.data.to_csv(self.output_path, index=False)
        print(f"El archivo limpio ha sido guardado en: {self.output_path}")
