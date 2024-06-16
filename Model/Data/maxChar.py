import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer

# Load the CSV file
df = pd.read_csv('/Users/mateo/Library/Mobile Documents/com~apple~CloudDocs/Desktop/Trabajos/Trabajos Mateo/Universidad/Universidad Privada Boliviana/Semestre VIII/5. Inteligencia Artificial/PF/CSV/filteredData.csv')

# Extract the 'text' column as the documents
documents = df['text'].tolist()

# Initialize TfidfVectorizer
vectorizer = TfidfVectorizer(max_features=100)  # Set max_features to desired number

# Fit and transform the documents
X = vectorizer.fit_transform(documents)

# Convert to dense array to see the actual values
dense_array = X.toarray()

print(dense_array)