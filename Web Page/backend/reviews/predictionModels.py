import pandas as pd
from keras.preprocessing.text import Tokenizer
from keras.preprocessing.sequence import pad_sequences
from keras.models import load_model
from transformers import pipeline
import environ
import sys
sys.path.append('../../Model/Data')
import modelInputPreprocess

class Model:
    def __init__(self):
        # Initialize django-environ
        self.env = environ.Env()
        environ.Env.read_env()
        
        # Load environment variables
        #self.KERAS_MODEL_PATH = self.env("KERAS_MODEL_PATH")
        
        # Load the Keras model
        self.model = load_model(r'C:\Users\PC\Documents\Dank\Model2Categories')

        # Load the transformer model
        self.classifier = pipeline("text-classification", model="Almancy/finetuning-emotion-model")
        
        # Initialize other parameters if needed
        self.maxLen = 250  # Maximum sequence length expected by the model

        self.wordTokenizer = self.createTokenizer()

    def preprocess_text(self, text, isTensor=False):
        text = modelInputPreprocess.preprocessTextInput(text)
        print(text)
        if (isTensor):
            # Tokenize and pad the input text
            sequence = self.wordTokenizer.texts_to_sequences([text])
            padded_sequence = pad_sequences(sequence, padding='post', maxlen=self.maxLen)
            
            return padded_sequence
        else:
            return text
        
    def createTokenizer(self):
        df = pd.read_csv(r'C:\Users\PC\Documents\Dank\preprocessedData2.csv')
        dataX = df['text']
        wordTokenizer = Tokenizer()
        wordTokenizer.fit_on_texts(dataX)
        return wordTokenizer
        
    def mapLabels(self, prediction):
        label_map = {
                "LABEL_0": "very_negative",
                "LABEL_1": "negative",
                "LABEL_2": "neutral",
                "LABEL_3": "positive",
                "LABEL_4": "very_positive"
            }

        highest_score_label = max(prediction[0], key=lambda x: x['score'])['label']
        mapped_label = label_map[highest_score_label]
        
        return mapped_label

    def predict_text(self, text):
        # Preprocess the text
        processed_text = self.preprocess_text(text, True)
        
        # Make prediction
        prediction = self.model.predict(processed_text)
        
        # Convert prediction to a category or class label
        predicted_category = prediction.argmax(axis=-1)

        category_map = {0: 'negative', 1: 'positive'}
        predicted_label = category_map[predicted_category[0]]

        return predicted_label
