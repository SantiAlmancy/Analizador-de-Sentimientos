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
        # Load the Keras model
        self.model = load_model('../../Resources/Model2Categories')
        # Load the transformer model
        self.classifier = pipeline("text-classification", model="Almancy/finetuning-emotion-model")
        # Maximum length for keras model
        self.maxLen = 250
        # Tokenizer created with data csv
        self.word_tokenizer = self.createTokenizer()

    def preprocess_text(self, text, is_tensor=False):
        text = modelInputPreprocess.preprocessTextInput(text)
        if (is_tensor):
            # Tokenize and pad the input text
            sequence = self.word_tokenizer.texts_to_sequences([text])
            padded_sequence = pad_sequences(sequence, padding='post', maxlen=self.maxLen)
            return padded_sequence
        else:
            return text
        
    def createTokenizer(self):
        df = pd.read_csv('../../Resources/preprocessedData2.csv')
        data_x = df['text']
        word_tokenizer = Tokenizer()
        word_tokenizer.fit_on_texts(data_x)
        return word_tokenizer
        
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
