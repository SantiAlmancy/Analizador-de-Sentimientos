from transformers import AutoModelForSequenceClassification, Trainer, TrainingArguments
from sklearn.metrics import accuracy_score, f1_score
import torch

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

    def train_model(self, output_dir, num_train_epochs=3, learning_rate=2e-5, batch_size=16):
        try:
            model = AutoModelForSequenceClassification.from_pretrained(self.model_checkpoint, num_labels=5)
            model.to(self.device)
            
            training_args = TrainingArguments(
                output_dir=output_dir,
                num_train_epochs=num_train_epochs,
                learning_rate=learning_rate,
                per_device_train_batch_size=batch_size,
                per_device_eval_batch_size=batch_size,
                weight_decay=0.01,
                eval_strategy="epoch",
                disable_tqdm=False,
                push_to_hub=True,
                report_to="none"
            )

            trainer = Trainer(
                model=model,
                args=training_args,
                train_dataset=self.train_dataset,
                eval_dataset=self.test_dataset,
                compute_metrics=self.compute_metrics,
                tokenizer=self.tokenizer
            )

            trainer.train()
            return trainer
        except Exception as e:
            print(f"Error training model: {e}")
            return None

    def compute_metrics(self, pred):
        labels = pred.label_ids
        preds = pred.predictions.argmax(-1)
        accuracy = accuracy_score(labels, preds)
        f1 = f1_score(labels, preds, average="weighted")
        return {"accuracy": accuracy, "f1": f1}