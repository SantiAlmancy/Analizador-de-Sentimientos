from datasets import Dataset, DatasetDict
from sklearn.model_selection import train_test_split

class DatasetHandler:
    def __init__(self, df):
        self.df = df

    def create_dataset(self):
        try:
            dataset = Dataset.from_pandas(self.df)
            return dataset
        except Exception as e:
            print(f"Error creating dataset: {e}")
            return None

    