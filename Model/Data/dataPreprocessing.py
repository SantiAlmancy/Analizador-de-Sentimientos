import os
import pandas as pd
import ast
from langdetect import detect
from langdetect.lang_detect_exception import LangDetectException

pathOriginalData = os.getenv('ORIGINAL_DATA_PATH')
print(pathOriginalData)

# Importing the data
data = pd.read_csv(pathOriginalData)

# Removing rows with null values
data.dropna()

print(data)