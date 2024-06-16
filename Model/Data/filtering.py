import pandas as pd
import re

def remove_punctuation(text):
    #Removing punctuation except for the exclamation character
    cleaned_text = re.sub(r'[^\w\s!]', '', text)
    cleaned_text = cleaned_text.strip()
    return cleaned_text