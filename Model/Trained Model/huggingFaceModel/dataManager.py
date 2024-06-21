import pandas as pd

class DataManager:
    def __init__(self, filepath):
        self.filepath = filepath

    def read_data(self):
        try:
            df = pd.read_csv(self.filepath, on_bad_lines='skip')
            return df
        except Exception as e:
            print(f"Error reading data: {e}")
            return None

