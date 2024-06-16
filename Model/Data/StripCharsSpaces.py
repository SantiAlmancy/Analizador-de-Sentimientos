import re
import os
import pandas as pd
from dotenv import load_dotenv, dotenv_values 

# (\\b[A-Za-z] \\b|\\b [A-Za-z]\\b):
# - \\b[A-Za-z] \\b: Matches a single alphabetic character [A-Za-z] surrounded by word boundaries \\b (i.e., not preceded or followed by other letters or digits).
# - |: Alternation operator to match either of the patterns separated by it.
# - \\b [A-Za-z]\\b: Matches a single alphabetic character [A-Za-z] preceded or followed by a space \\b and followed or preceded by word boundaries \\b.
# - '': Replace the matched patterns with an empty string, effectively removing them from the text.
def singleCharacterRemoval(sentence):
  sentence = re.sub('(\\b[A-Za-z] \\b|\\b [A-Za-z]\\b)', '', sentence)
  return sentence

# Creates a regex pattern to match any character from charsList, treating them literally.
def specialCharacterRemoval(sentence, charsList):
   regex_pattern = '[' + re.escape(''.join(charsList)) + ']'
   return re.sub(regex_pattern, ' ', sentence)

# \s+ matches one or more whitespace characters.
def removeMultipleSpaces(sentence):
  sentence = re.sub(r'\s+', ' ', sentence)
  return sentence

if __name__ == "__main__":
    # Importing the data
    load_dotenv() 
    filePath = os.getenv("FILTERED_DATA_PATH")
    df = pd.read_csv(filePath)
    print(df)

    # Apply functions:
    df['title'] = df['title'].apply(singleCharacterRemoval)
    df['text'] = df['text'].apply(singleCharacterRemoval)
    
    special_characters_to_remove = [
    '~', '`', '@', '#', '$', '%', '^', '&', '*', '(', ')',
    '_', '+', '=', '{', '}', '[', ']', '|', ':', ';', '"',
    "'", '<', '>', ',', '.', '?', '/', '-', '\n', '\t', '\r', '\x0b', '\x0c']
    df['title'] = df['title'].apply(lambda x: specialCharacterRemoval(x, special_characters_to_remove))
    df['text'] = df['text'].apply(lambda x: specialCharacterRemoval(x, special_characters_to_remove))

    df['title'] = df['title'].apply(removeMultipleSpaces)
    df['text'] = df['text'].apply(removeMultipleSpaces)

    # Print result
    print(df)
