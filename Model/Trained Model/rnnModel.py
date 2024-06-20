import os
import pandas as pd
import keras
from numpy import asarray
from numpy import zeros
from sklearn.model_selection import train_test_split
from keras.preprocessing.text import Tokenizer
from keras.preprocessing.sequence import pad_sequences

# Creating embeddings dictionary with pretrained data
def createEmbeddingsDictionary():
    embeddingsDictionary = dict()
    path = os.getenv("EMBEDDING_FILE_PATH")
    gloveFile = open(path, encoding="utf8")

    for line in gloveFile:
        records = line.split()
        word = records[0]
        vector_dimensions = asarray(records[1:], dtype='float32')
        embeddingsDictionary [word] = vector_dimensions
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

if __name__ == "__main__":
    # Importing the data
    dataPath = os.getenv("PREPROCESSED_DATA_PATH")
    df = pd.read_csv(dataPath)

    # Number of samples per group
    nSamples = 1000
    randomState = 42  # Set a seed for reproducibility

    # Select 1000 samples of 'text' for each unique value in 'overall'
    df = df.groupby('overall', group_keys=False).apply(lambda x: x.sample(min(len(x), nSamples), random_state=randomState))
    
    # Shuffle the data to remove grouping by 'overall'
    df = df.sample(frac=1, random_state=randomState).reset_index(drop=True)

    #overall_counts = df['overall'].value_counts()
    #print(overall_counts)
    #print(df)

    # Creating data and its labels to training
    dataX = df['text']
    dataY = keras.utils.to_categorical(df['overall'] - 1, 5) # Converting to one-hot vector to classify the data
    #print(dataY)

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
    maxlen = 100
    xTrain = pad_sequences(xTrain, padding='post', maxlen=maxlen)
    xTest = pad_sequences(xTest, padding='post', maxlen=maxlen)

    # Creating embedding matrix
    embeddingMatrix = createEmbeddingMatrix(vocabLength, wordTokenizer)

    print(embeddingMatrix.shape)

