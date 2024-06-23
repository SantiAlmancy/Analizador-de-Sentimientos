# reviews/model.py
import pandas as pd
import numpy as np
from keras_preprocessing.text import Tokenizer
from keras_preprocessing.sequence import pad_sequences
from keras.models import load_model
from transformers import pipeline
import environ
import sys
sys.path.append(r'C:\Users\PC\Documents\IA Web Page\Analizador-de-Sentimientos\Model\Data')
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
        self.classifier = pipeline("text-classification", model="Almancy/finetuning-emotion-model-5")
        
        # Initialize other parameters if needed
        self.maxLen = 250  # Maximum sequence length expected by the model

