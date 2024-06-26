import os
from dotenv import load_dotenv
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer

# Load environment variables from .env file
load_dotenv()

# Get the filtered CSV file path from environment variables
FILTERED_DATA_PATH = os.getenv('FILTERED_DATA_PATH')

# Use the path to read the CSV file
df = pd.read_csv(FILTERED_DATA_PATH, encoding='utf-8')

# Extract the 'text' column as the documents
documents = df['text'].tolist()

# Initialize TfidfVectorizer
vectorizer = TfidfVectorizer(maxFeatures=100)  # Set maxFeatures to desired number

# Fit and transform the documents
X = vectorizer.fit_transform(documents)

# Convert to dense array to see the actual values
denseArray = X.toarray()

print(denseArray)