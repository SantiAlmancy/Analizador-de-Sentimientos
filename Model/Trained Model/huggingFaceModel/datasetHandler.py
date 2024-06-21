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

    def split_dataset(self, test_size=0.2):
        try:
            dataset = self.create_dataset()
            train_test_split = dataset.train_test_split(test_size=test_size)
            return DatasetDict({
                'train': train_test_split['train'],
                'test': train_test_split['test']
            })
        except Exception as e:
            print(f"Error splitting dataset: {e}")
            return None
