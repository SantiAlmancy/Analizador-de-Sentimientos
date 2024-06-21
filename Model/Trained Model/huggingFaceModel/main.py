from transformers import AutoTokenizer, pipeline
import matplotlib.pyplot as plt
from huggingface_hub import login

from dataManager import DataManager
from datasetHandler import DatasetHandler
from modelTrainer import ModelTrainer

import pandas as pd

def main():
    checkpoint = "distilbert-base-uncased"
    tokenizer = AutoTokenizer.from_pretrained(checkpoint)
    filepath = 'C:/Users/PC/Documents/IA/Model/Trained Model/huggingFaceModel/preprocessedData5.csv'
    output_dir = "finetuning-emotion-model-5"

    login(token="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")
    data_manager = DataManager(filepath)
    df = data_manager.read_data()
    if df is None:
        return

    df = data_manager.preprocess_data(df)
    if df is None:
        return

    dataset_handler = DatasetHandler(df)
    datasets = dataset_handler.split_dataset(test_size=0.2)
    if datasets is None:
        return

    def tokenize_function(batch):
        return tokenizer(batch["text"], padding=True, truncation=True)

    tokenized_datasets = datasets.map(tokenize_function, batched=True)
    tokenized_datasets = tokenized_datasets.remove_columns(["text"])

    print(tokenized_datasets['train'].column_names)

    

if __name__ == "__main__":
    main()