import pandas as pd
import keras
from sklearn.model_selection import train_test_split
from keras.preprocessing.text import Tokenizer
from keras_preprocessing.sequence import pad_sequences
from keras.models import load_model
import argparse

def main(csv_path, model_path):
    # Load the data
    df = pd.read_csv(csv_path)
    randomState = 42
    dataX = df['text']
    dataY = keras.utils.to_categorical(df['overall'] - 1, 3)  # Converting to one-hot vector to classify the data

    # Splitting the data
    xTrain, xTest, yTrain, yTest = train_test_split(dataX, dataY, test_size=0.30, random_state=randomState)

    # Tokenizing and converting text to numerical sequences
    wordTokenizer = Tokenizer()
    wordTokenizer.fit_on_texts(xTrain)

    xTrain = wordTokenizer.texts_to_sequences(xTrain)
    xTest = wordTokenizer.texts_to_sequences(xTest)

    # Adding 1 to store dimensions for words for which no pretrained word embeddings exist
    vocabLength = len(wordTokenizer.word_index) + 1

    # Padding all reviews to fixed length 100
    maxLen = 250
    xTrain = pad_sequences(xTrain, padding='post', maxlen=maxLen)
    xTest = pad_sequences(xTest, padding='post', maxlen=maxLen)

    # Load the model
    loaded_model = load_model(model_path)

    # Use the loaded model for predictions or evaluation
    loss, accuracy = loaded_model.evaluate(xTest, yTest)
    print(f'Loaded model accuracy: {accuracy}')

if __name__ == "__main__":
    # Set up argument parser
    parser = argparse.ArgumentParser(description='Process CSV and model paths.')
    parser.add_argument('csv_path', type=str, help='Path to the CSV file')
    parser.add_argument('model_path', type=str, help='Path to the trained model file')

    args = parser.parse_args()

    main(args.csv_path, args.model_path)
