import os
import pandas as pd
from dotenv import load_dotenv 
from csvGeneration import distributeData
from htmlTagsRemoval import remove_html_tags
#from maxChar import singleCharacterRemoval, removeMultipleSpaces

from lemmatization import lemmatizer
from stopWords import removeStopWords
from filtering import convert_number_words, num_words
from StripCharsSpaces import singleCharacterRemoval, specialCharacterRemoval, removeMultipleSpaces


if __name__ == "__main__":
    # Importing the data
    load_dotenv() 
    filePath = os.getenv("CSV_FILE_PATH")
    df = pd.read_csv(filePath)
    df = df.head(10)

    for index, text_value in df['text'].items():
        print(index, text_value)

    
    # Apply functions:
    # Stop Words Removal
    df['text'] = df['text'].apply(removeStopWords)

    # Lemmatization:
    df['text'] = df['text'].apply(lemmatizer)

    # Single Characters Removal
    df['text'] = df['text'].apply(singleCharacterRemoval)

    # Remove HTML Tags
    df['text'] = df['text'].apply(remove_html_tags)

    # Convert words to numbers
    df['text'] = df['text'].apply(convert_number_words)
    
    # Special Characteres Removal
    special_characters_to_remove = [
    '~', '`', '@', '#', '$', '%', '^', '&', '*', '(', ')',
    '_', '+', '=', '{', '}', '[', ']', '|', ':', ';', '"',
    "'", '<', '>', ',', '.', '/', '-', '\n', '\t', '\r', '\x0b', '\x0c']
    df['text'] = df['text'].apply(lambda x: specialCharacterRemoval(x, special_characters_to_remove))

    # Multiples Spaces Removal
    df['text'] = df['text'].apply(removeMultipleSpaces)

    # Print result
    for index, text_value in df['text'].items():
        print("-------------------------------------------------------------")
        print(index, text_value)
