import os
import pandas as pd
import ast
import py3langid as langid

def detectLanguage(text):
    lang, _ = langid.classify(text)
    return lang
    
def extractOverall(ratingsText):
    ratingsDictionary = ast.literal_eval(ratingsText)
    return ratingsDictionary.get('overall', None)

if __name__ == "__main__":
    pathOriginalData = os.getenv('ORIGINAL_DATA_PATH')

    # Importing the data
    data = pd.read_csv(pathOriginalData)

    # Adding a column 'overall' with the extracted value from the column 'ratings'.
    data['overall'] = data['ratings'].apply(extractOverall)

    # Removing rows with null values
    data.dropna()

    # Adding a column 'language' with the language of the text in the column 'text'
    data['language'] = data['text'].apply(detectLanguage)

    # Filtering the language of data
    data = data[data['language'] == 'en']

    print(data)

    pathFilteredData = os.getenv('FILTERED_DATA_PATH')

    # Generating a csv file without index numbers
    data.to_csv(pathFilteredData, index=False)