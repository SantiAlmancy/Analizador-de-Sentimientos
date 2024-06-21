from transformers import AutoModelForSequenceClassification, Trainer, TrainingArguments
from sklearn.metrics import accuracy_score, f1_score
import torch

# Clase para manejar el entrenamiento del modelo
class ModelTrainer:
    def __init__(self, model_checkpoint, train_dataset, test_dataset, tokenizer):
        self.model_checkpoint = model_checkpoint
        self.train_dataset = train_dataset
        self.test_dataset = test_dataset
        self.tokenizer = tokenizer
        self.device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
        if torch.cuda.is_available():
            print(f"Using CUDA with GPU: {torch.cuda.get_device_name(0)}")
        else:
            print("CUDA is not available. Training on CPU...")

    def compute_metrics(self, pred):
        labels = pred.label_ids
        preds = pred.predictions.argmax(-1)
        accuracy = accuracy_score(labels, preds)
        f1 = f1_score(labels, preds, average="weighted")
        return {"accuracy": accuracy, "f1": f1}