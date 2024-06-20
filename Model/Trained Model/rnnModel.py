import os
import pandas as pd

if __name__ == "__main__":
    # Importing the data
    dataPath = os.getenv("PREPROCESSED_DATA_PATH")
    df = pd.read_csv(dataPath)

    # Number of samples per group
    n_samples = 1000
    random_state = 42  # Set a seed for reproducibility

    # Select 1000 samples of 'text' for each unique value in 'overall'
    df = df.groupby('overall', group_keys=False).apply(lambda x: x.sample(min(len(x), n_samples), random_state=random_state))

    #overall_counts = df['overall'].value_counts()
    #print(overall_counts)
