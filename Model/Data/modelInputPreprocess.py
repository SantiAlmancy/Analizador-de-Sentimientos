from lemmatization import lemmatizer
from stopWords import removeStopWords
from filtering import convertNumberWords
from StripCharsSpaces import singleCharacterRemoval, specialCharacterRemoval, removeMultipleSpaces
import pandas as np

def preprocessTextInput(text):
    text = removeStopWords(text)
    text = lemmatizer(text)
    text = singleCharacterRemoval(text)
    text = convertNumberWords(text)
    specialCharactersToRemove = [
    '~', '`', '@', '#', '$', '%', '^', '&', '*', '(', ')',
    '_', '+', '=', '{', '}', '[', ']', '|', ':', ';', '"',
    "'", '<', '>', ',', '.', '/', '-', '\n', '\t', '\r', '\x0b', '\x0c']
    text = specialCharacterRemoval(text, specialCharactersToRemove)
    text = removeMultipleSpaces(text)
    return text