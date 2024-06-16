import os
from dotenv import load_dotenv
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer

# Load environment variables from .env file
load_dotenv()

# Get the CSV file path from environment variables
CSV_FILE_PATH = os.getenv('CSV_FILE_PATH')

# Use the path to read the CSV file
df = pd.read_csv(CSV_FILE_PATH, encoding='utf-8')

# Extract the 'text' column as the documents
documents = df['text'].tolist()

# Initialize TfidfVectorizer
vectorizer = TfidfVectorizer(max_features=100)  # Set max_features to desired number

# Fit and transform the documents
X = vectorizer.fit_transform(documents)

# Convert to dense array to see the actual values
dense_array = X.toarray()

print(dense_array)