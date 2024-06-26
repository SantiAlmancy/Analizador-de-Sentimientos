import pandas as pd
import keras
from sklearn.model_selection import train_test_split
from keras.preprocessing.text import Tokenizer
from keras.preprocessing.sequence import pad_sequences
from keras.models import load_model
import argparse

string2 = "My stay at the Grand Palace Hotel was extraordinary. The staff were exceptionally welcoming, the room was immaculate, and the views were stunning. The complimentary breakfast was delicious and varied. I felt pampered throughout my stay. Definitely coming back!"
def predict_text(text, model, wordTokenizer, maxLen):
    # Convertir el texto en una secuencia numérica
    sequence = wordTokenizer.texts_to_sequences([text])
    
    # Rellenar la secuencia para que tenga la misma longitud que los datos de entrenamiento
    padded_sequence = pad_sequences(sequence, padding='post', maxlen=maxLen)
    
    # Hacer la predicción
    prediction = model.predict(padded_sequence)
    
    # Convertir la predicción a una categoría
    predicted_category = prediction.argmax(axis=-1)
    
    # Mapeo de la categoría predicha a las etiquetas originales
    category_map = {0: 'Negativa', 1: 'Positiva'}
    predicted_label = category_map[predicted_category[0]]
    
    return predicted_label

# Load the data
df = pd.read_csv(r'C:\Users\Ale\UPB\Inteligencia Artificial\preprocessedData2.csv')
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
loaded_model = load_model(r'C:\Users\Ale\UPB\Inteligencia Artificial\Model2Categories')

# Ejemplo de uso
#text = "El producto es excelente y cumple con todas mis expectativas."
predicted_label = predict_text(string2, loaded_model, wordTokenizer, maxLen)
print(f'Predicted label: {predicted_label}')