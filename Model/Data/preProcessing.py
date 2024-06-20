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
    filePath = os.getenv("FILTERED_DATA_PATH")
    df = pd.read_csv(filePath)
    
    # Apply functions:
    # Stop Words Removal
    df['text'] = df['text'].apply(removeStopWords)
    df['title'] = df['title'].apply(removeStopWords)

    # Lemmatization:
    df['text'] = df['text'].apply(lemmatizer)
    df['title'] = df['title'].apply(lemmatizer)

    # Single Characters Removal
    df['text'] = df['text'].apply(singleCharacterRemoval)
    df['title'] = df['title'].apply(singleCharacterRemoval)

    # Remove HTML Tags
    df['text'] = df['text'].apply(remove_html_tags)
    df['title'] = df['title'].apply(remove_html_tags)

    # Convert words to numbers
    df['text'] = df['text'].apply(convert_number_words)
    df['title'] = df['title'].apply(convert_number_words)
    
    # Special Characteres Removal
    special_characters_to_remove = [
    '~', '`', '@', '#', '$', '%', '^', '&', '*', '(', ')',
    '_', '+', '=', '{', '}', '[', ']', '|', ':', ';', '"',
    "'", '<', '>', ',', '.', '/', '-', '\n', '\t', '\r', '\x0b', '\x0c']
    df['text'] = df['text'].apply(lambda x: specialCharacterRemoval(x, special_characters_to_remove))
    df['title'] = df['title'].apply(lambda x: specialCharacterRemoval(x, special_characters_to_remove))

    # Multiples Spaces Removal
    df['text'] = df['text'].apply(removeMultipleSpaces)
    df['title'] = df['title'].apply(removeMultipleSpaces)

    # Columns selection
    df = df[['title', 'text', 'overall']]

    # Preprocessed csv file generation
    pathPreprocesseddData = os.getenv('PREPROCESSED_DATA_PATH')
    df.to_csv(pathPreprocesseddData, index=False)  
