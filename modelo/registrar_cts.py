import pandas as pd


class CsvProcessor:
    def __init__(self):
        self.df = pd.DataFrame()

    def read_csv(self, file_path):
        self.df = pd.read_csv(file_path)
        return self.df

