import pandas as pd
import re
from nltk.tokenize import word_tokenize
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Function to clean text
def clean_text(text):
    # Remove special characters except ! and ?
    cleaned_text = re.sub(r'[^a-zA-Z0-9!? ]+', '', text)
    # Remove [U+32] explicitly if present
    cleaned_text = cleaned_text.replace('\u0020', '')  # Unicode for [U+32] is space
    return cleaned_text

# Path to your CSV file from .env
input_csv_path = os.getenv('CSV_FILE_PATH')
output_csv_path = 'filteredData_cleaned.csv'

# Read CSV into a DataFrame
df = pd.read_csv(input_csv_path, encoding='utf-8')

# Apply cleaning to each cell in the DataFrame
cleaned_df = df.applymap(clean_text)

# Write the cleaned DataFrame back to a new CSV
cleaned_df.to_csv(output_csv_path, index=False, encoding='utf-8')

print("CSV cleaning completed.")