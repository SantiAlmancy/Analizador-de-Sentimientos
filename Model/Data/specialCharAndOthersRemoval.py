import csv
import re
from nltk.tokenize import word_tokenize

# Function to clean text
def clean_text(text):
    # Remove special characters except ! and ?
    cleaned_text = re.sub(r'[^a-zA-Z0-9!? ]+', '', text)
    # Remove [U+32] explicitly if present
    cleaned_text = cleaned_text.replace('\u0020', '')  # Unicode for [U+32] is space
    return cleaned_text

# Path to your CSV file
input_csv_path = 'path/to/your/input.csv'
output_csv_path = 'path/to/your/output.csv'

# Read CSV, clean data, and write to a new CSV
with open(input_csv_path, mode='r', encoding='utf-8') as infile, \
     open(output_csv_path, mode='w', encoding='utf-8', newline='') as outfile:
    reader = csv.reader(infile)
    writer = csv.writer(outfile)
    
    for row in reader:
        # Apply cleaning to each cell in the row
        cleaned_row = [clean_text(cell) for cell in row]
        writer.writerow(cleaned_row)

print("CSV cleaning completed.")