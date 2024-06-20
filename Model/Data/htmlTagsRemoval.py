import csv
from bs4 import BeautifulSoup
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

def remove_html_tags(input_string):
    # Check if input_string is indeed a string and looks like it might contain HTML
    if isinstance(input_string, str) and '<' in input_string and '>' in input_string:
        soup = BeautifulSoup(input_string, 'html.parser')
        return soup.get_text()
    # If input_string doesn't look like HTML, return it unchanged
    return input_string

def clean_csv_column(input_csv_path, output_csv_path, column_index):
    with open(input_csv_path, mode='r', encoding='utf-8') as infile, \
         open(output_csv_path, mode='w', newline='', encoding='utf-8') as outfile:
        reader = csv.reader(infile)
        writer = csv.writer(outfile)

        for row in reader:
            if row:  # Check if row is not empty
                # Clean the HTML content in the specified column
                row[column_index] = remove_html_tags(row[column_index])
            writer.writerow(row)

# Example usage:
#input_csv_path = os.getenv('CSV_FILE_PATH')  # Get the path from .env file
#output_csv_path = 'cleaned_output.csv'  # Path to your output CSV file
#column_index = 1  # Index of the column containing HTML content (0-based index)

#clean_csv_column(input_csv_path, output_csv_path, column_index)