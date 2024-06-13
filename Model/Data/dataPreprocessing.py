import os
import pandas as pd
import ast
import py3langid as langid
import matplotlib.pyplot as plt
import matplotlib.cm as cm 

def detectLanguage(text):
    lang, _ = langid.classify(text)
    return lang
    
def extractOverall(ratingsText):
    ratingsDictionary = ast.literal_eval(ratingsText)
    return ratingsDictionary.get('overall', None)

def showDataDistribution(datafrane,columnName,title):
    # Counting the quantity of data according the values from the column overall
    counts = datafrane[columnName].value_counts()
    print(counts)

    # Defining a predefined color palette (in this case tab10)
    colors = plt.get_cmap('tab10').colors[:len(counts)]

    # Creating bar chart
    plt.figure(figsize=(10, 6))
    counts.plot(kind='bar', color=colors)
    plt.title(f'Values distribution of "{columnName}"')
    plt.xlabel(f'Value "{columnName}"')
    plt.ylabel('Quantity')
    plt.suptitle(title, fontsize=17)
    plt.show()

if __name__ == "__main__":
    '''
    pathOriginalData = os.getenv('ORIGINAL_DATA_PATH')

    # Importing the data
    data = pd.read_csv(pathOriginalData)

    # Removing rows with null values
    data.dropna()

    # Adding a column 'language' with the language of the text in the column 'text'
    data['language'] = data['text'].apply(detectLanguage)

    # Filtering the language of data
    data = data[data['language'] == 'en']

    # Adding a column 'overall' with the extracted value from the column 'ratings'.
    data['overall'] = data['ratings'].apply(extractOverall)

  
    
    data = data[['title', 'text', 'offering_id', 'num_helpful_votes', 'overall']]

    #pathFilteredData = os.getenv('FILTERED_DATA_PATH')

    # Generating a csv file without index numbers
    #data.to_csv(pathFilteredData, index=False)
    '''

    data = pd.read_csv("filteredData.csv")

    # Filtering important columns
    data = data[['title', 'text', 'offering_id', 'num_helpful_votes', 'overall']]

    # Showing the initial data distribution after the language filtering
    showDataDistribution(data,'overall','Initial data distribution')