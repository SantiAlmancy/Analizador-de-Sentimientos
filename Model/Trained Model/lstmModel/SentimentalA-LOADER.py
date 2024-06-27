import os
import pandas as pd
import keras
from sklearn.model_selection import train_test_split
from keras.preprocessing.text import Tokenizer
from keras.preprocessing.sequence import pad_sequences
from keras.models import load_model

def predictText(text, model, wordTokenizer, maxLen):
    # Convert the text into a numerical sequence
    sequence = wordTokenizer.texts_to_sequences([text])
    
    # Pad the sequence to match the length of the training data
    paddedSequence = pad_sequences(sequence, padding='post', maxlen=maxLen)
    
    # Make the prediction
    prediction = model.predict(paddedSequence)
    
    # Convert the prediction to a category
    predictedCategory = prediction.argmax(axis=-1)
    
    # Map the predicted category to the original labels
    categoryMap = {0: 'Negative', 1: 'Positive'}
    predictedLabel = categoryMap[predictedCategory[0]]
    
    return predictedLabel

if __name__ == "__main__":
    # Load the data with TWO categories
    PREPROCESSED_DATA_PATH = os.getenv("PREPROCESSED_DATA_PATH")
    df = pd.read_csv(PREPROCESSED_DATA_PATH)
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

    # Padding all reviews to fixed length 250
    maxLen = 250
    xTrain = pad_sequences(xTrain, padding='post', maxlen=maxLen)
    xTest = pad_sequences(xTest, padding='post', maxlen=maxLen)

    # Load the model
    MODEL_PATH = os.getenv("MODEL_PATH")
    loadedModel = load_model(MODEL_PATH)

    # Example of use
    string = "My stay at the Grand Palace Hotel was extraordinary. The staff were exceptionally welcoming, the room was immaculate, and the views were stunning. The complimentary breakfast was delicious and varied. I felt pampered throughout my stay. Definitely coming back!"
    predictedLabel = predictText(string, loadedModel, wordTokenizer, maxLen)
    print(f'Predicted label: {predictedLabel}')