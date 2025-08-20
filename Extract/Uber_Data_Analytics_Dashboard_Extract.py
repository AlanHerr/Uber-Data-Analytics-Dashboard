import requests
import pandas as pd 
import numpy as np

class uberExtractor:
    def __init__ (self, csv_path):
        self.csv = csv_path
    
    def  queries (self):
        data = pd.read_csv (self.csv)

    def response ():
        return data.head(5)

    
    