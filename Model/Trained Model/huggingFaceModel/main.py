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

    model_trainer = ModelTrainer(checkpoint, tokenized_datasets['train'], tokenized_datasets['test'], tokenizer)
    trainer = model_trainer.train_model(output_dir=output_dir)

    if trainer is None:
        return

    trainer.push_to_hub(commit_message="Training completed")

    classifier = pipeline("text-classification", model=output_dir)
    pred = classifier("I don't know how to feel, the hotel was regular, not many rooms but they were clean",
                      return_all_scores=True)
    labels = ["Enojado", "Triste", "Indiferente", "Sorprendido", "Feliz"]
    df = pd.DataFrame(pred[0])
    plt.bar(labels, 100 * df["score"])
    plt.show()

if __name__ == "__main__":
    main()