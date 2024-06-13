import os
import pandas as pd
import ast
import py3langid as langid
import matplotlib.pyplot as plt
import matplotlib.cm as cm 

def detectLanguage(text):
    # Using langid to classify the text and detect the language
    lang, _ = langid.classify(text)
    return lang
    
def extractOverall(ratingsText):
    # Returns the value associated with the 'overall'
    ratingsDictionary = ast.literal_eval(ratingsText)
    return ratingsDictionary.get('overall', None)

def trimTitle(title):
    # Returning the title without the first 3 and the last 3 characters
    return title[3:-3] if len(title) > 6 else ""

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

def distributeData(dataframe):
    # Filter out records where 'overall' is 0
    filteredData = dataframe[dataframe['overall'] != 0]

    # Count the number of reviews for each unique 'overall' value
    counts = filteredData['overall'].value_counts()

    # Calculate the minimum count across all 'overall' values
    minCount = counts.min()

    # Sort by 'num_helpful_votes' (descending) within each 'overall' group (ascending)
    sortedData = filteredData.sort_values(by=['overall', 'num_helpful_votes'], ascending=[True, False])

    # Group by 'overall' and take the first min_count rows from each group
    newData = sortedData.groupby('overall').head(minCount).reset_index(drop=True)

    # Shuffle the data to remove grouping by 'overall'
    newData = newData.sample(frac=1).reset_index(drop=True)

    return newData


if __name__ == "__main__":
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

    # Filtering important columns
    data = data[['title', 'text', 'offering_id', 'num_helpful_votes', 'overall']]
    print(data)

    # Showing the initial data distribution after the language filtering
    showDataDistribution(data,'overall','Initial data distribution')

    data = distributeData(data)

    # Removing special leading and trailing characters from the 'title' column
    data['title'] = data['title'].apply(trimTitle)

    print(data)

    # Showing the new data distribution after the distribution of data
    showDataDistribution(data,'overall','New data distribution') 

    # Generating a csv file of new data without index numbers
    pathFilteredData = os.getenv('FILTERED_DATA_PATH')
    data.to_csv(pathFilteredData, index=False)   