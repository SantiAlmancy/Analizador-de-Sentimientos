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

    def preprocess_data(self, df):
        try:
            df = df[['text', 'overall']]
            df = df.copy()
            df.rename(columns={'overall': 'label'}, inplace=True)
            df = df.dropna(subset=['label'])
            df['label'] = df['label'].astype(int) - 1
            return df
        except Exception as e:
            print(f"Error preprocessing data: {e}")
            return None
