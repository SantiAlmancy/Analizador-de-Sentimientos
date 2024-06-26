import os
import pandas as pd
import keras
from numpy import asarray
from numpy import zeros
from sklearn.model_selection import train_test_split
from keras.preprocessing.text import Tokenizer
from keras.preprocessing.sequence import pad_sequences
from keras.models import Sequential
from keras.layers import Embedding, LSTM, Dense, Dropout, Bidirectional
from keras.regularizers import l2

# Creating embeddings dictionary with pretrained data
def createEmbeddingsDictionary():
    embeddingsDictionary = dict()
    EMBEDDING_FILE_PATH = os.getenv("EMBEDDING_FILE_PATH")
    gloveFile = open(EMBEDDING_FILE_PATH, encoding="utf8")

    for line in gloveFile:
        records = line.split()
        word = records[0]
        vectorDimensions = asarray(records[1:], dtype='float32')
        embeddingsDictionary [word] = vectorDimensions
    gloveFile.close()

    return embeddingsDictionary

# Creating embedding matrix with our vocabulary and the embeddings dictionary
def createEmbeddingMatrix(vocabLength, wordTokenizer):
    embeddingsDictionary = createEmbeddingsDictionary()
    embeddingMatrix = zeros((vocabLength, 100))
    for word, index in wordTokenizer.word_index.items():
        embeddingVector = embeddingsDictionary.get(word)
        if embeddingVector is not None:
            embeddingMatrix[index] = embeddingVector

    return embeddingMatrix

# Creation of the model
def createLSTMModel(embeddingMatrix, vocabLength, maxLen):
    model = Sequential()
    model.add(Embedding(vocabLength, 100, weights=[embeddingMatrix], input_length=maxLen, trainable=True))
    model.add(Bidirectional(LSTM(256, return_sequences=True, kernel_regularizer=l2(0.03))))
    model.add(Dropout(0.2))  # Adding Dropout for regularization
    model.add(Bidirectional(LSTM(128, return_sequences=False, kernel_regularizer=l2(0.03))))
    model.add(Dense(2, activation='sigmoid'))

    model.compile(optimizer='RMSprop', loss='categorical_crossentropy', metrics=['accuracy'])
    return model

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
    # Importing the preprocessed data with TWO categories
    PREPROCESSED_DATA_PATH = os.getenv("PREPROCESSED_DATA_PATH")
    df = pd.read_csv(PREPROCESSED_DATA_PATH)

    randomState = 42  # Set a seed for reproducibility

    # The following lines must be commented to train the model with all the data
    # Number of samples per group
    #nSamples = 8000

    # Select 1000 samples of 'text' for each unique value in 'overall'
    #df = df.groupby('overall', group_keys=False).apply(lambda x: x.sample(min(len(x), nSamples), random_state=randomState))

    # Shuffle the data to remove grouping by 'overall'
    #df = df.sample(frac=1, random_state=randomState).reset_index(drop=True)

    # Creating data and its labels to training
    # Apply the label adjustment function to create adjusted labels
    dataX = df['text']
    dataY = keras.utils.to_categorical(df['overall'] -1, 2) # Converting to one-hot vector to classify the data

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

    # Creating embedding matrix
    embeddingMatrix = createEmbeddingMatrix(vocabLength, wordTokenizer)

    # Creating the model
    model = createLSTMModel(embeddingMatrix, vocabLength, maxLen)

    # Training the model
    model.fit(xTrain, yTrain, epochs=14, validation_split=0.2)

    # Evaluating the model
    loss, accuracy = model.evaluate(xTest, yTest)
    print('Test Loss:', loss)
    print('Test Accuracy:',  accuracy)

    # Saving the model
    MODEL_PATH = os.getenv("MODEL_PATH")
    model.save(MODEL_PATH)

    # Example of use
    string = "wonderful service nice location"
    predictedLabel = predictText(string, model, wordTokenizer, maxLen)
    print(f'Predicted label: {predictedLabel}')