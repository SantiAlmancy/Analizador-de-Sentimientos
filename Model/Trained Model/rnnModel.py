import os
import pandas as pd
import keras

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
