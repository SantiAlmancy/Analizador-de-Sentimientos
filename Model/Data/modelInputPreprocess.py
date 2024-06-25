from lemmatization import lemmatizer
from stopWords import removeStopWords
from filtering import convert_number_words
from StripCharsSpaces import singleCharacterRemoval, specialCharacterRemoval, removeMultipleSpaces
import pandas as np

def preprocessTextInput(text):
    text = removeStopWords(text)
    text = lemmatizer(text)
    text = singleCharacterRemoval(text)
    text = convert_number_words(text)
    special_characters_to_remove = [
    '~', '`', '@', '#', '$', '%', '^', '&', '*', '(', ')',
    '_', '+', '=', '{', '}', '[', ']', '|', ':', ';', '"',
    "'", '<', '>', ',', '.', '/', '-', '\n', '\t', '\r', '\x0b', '\x0c']
    text = specialCharacterRemoval(text, special_characters_to_remove)
    text = removeMultipleSpaces(text)
    return text