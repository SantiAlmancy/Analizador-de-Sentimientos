import pandas as pd
import re

def remove_punctuation(text):
    #Removing punctuation except for the exclamation character
    cleaned_text = re.sub(r'[^\w\s!]', '', text)
    cleaned_text = cleaned_text.strip()
    return cleaned_text

num_words = {
    'zero': '0', 'one': '1', 'two': '2', 'three': '3', 'four': '4', 'five': '5',
    'six': '6', 'seven': '7', 'eight': '8', 'nine': '9', 'ten': '10',
    'eleven': '11', 'twelve': '12', 'thirteen': '13', 'fourteen': '14',
    'fifteen': '15', 'sixteen': '16', 'seventeen': '17', 'eighteen': '18',
    'nineteen': '19', 'twenty': '20', 'thirty': '30', 'forty': '40',
    'fifty': '50', 'sixty': '60', 'seventy': '70', 'eighty': '80', 'ninety': '90',
    'hundred': '100', 'thousand': '1000', 'million': '1000000', 'billion': '1000000000'
}

def convert_number_words(text):
    #Replacing written numbers for literal ones
    for word, digit in num_words.items():
        text = re.sub(r'\b' + word + r'\b', digit, text)
    return text


def clean_dataset(df, text_column):
    #processing the dataset filtering based on previous methods
    df['cleaned_text'] = df[text_column].apply(convert_number_words).apply(remove_punctuation)
    return df