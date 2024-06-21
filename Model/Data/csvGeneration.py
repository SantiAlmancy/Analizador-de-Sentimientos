import os
import pandas as pd
import ast
import py3langid as langid
import matplotlib.pyplot as plt
import matplotlib.cm as cm 

# Returns the number of words in the text
def countWords(text):
    return len(text.split())

def detectLanguage(text):
    # Using langid to classify the text and detect the language
    lang, _ = langid.classify(text)
    return lang
    
def extractOverall(ratingsText):
    # Returns the value associated with the 'overall'
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

def distributeDataFive(dataframe):
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

def distributeDataThree(dataframe):
    # Filter out records where 'overall' is 0
    filteredData = dataframe[dataframe['overall'] != 0]

    # Create a dataframe for each category
    dfNeg = filteredData[filteredData['overall'] < 3]
    dfNeu = filteredData[filteredData['overall'] == 3]
    dfPos = filteredData[filteredData['overall'] > 3]

    # Sort each dataframe in descending order based on 'num_helpful_votes'
    dfNeg = dfNeg.sort_values(by='num_helpful_votes', ascending=False)
    dfNeu = dfNeu.sort_values(by='num_helpful_votes', ascending=False)
    dfPos = dfPos.sort_values(by='num_helpful_votes', ascending=False)

    # Get the number of rows in each dataframe
    countNeg = dfNeg.shape[0]
    countNeu = dfNeu.shape[0]
    countPos = dfPos.shape[0]
    minCount = min(countNeg, countNeu, countPos)

    # Take the first minCount rows from each dataframe
    dfNeg = dfNeg.head(minCount)
    dfNeu = dfNeu.head(minCount)
    dfPos = dfPos.head(minCount)

    # Change the values of 'overall' to the new categories
    dfNeg['overall'] = 1
    dfNeu['overall'] = 2
    dfPos['overall'] = 3

    # Combine the three dataframes
    combinedDf = pd.concat([dfNeg, dfNeu, dfPos])

    # Shuffle the dataframe
    shuffledDf = combinedDf.sample(frac=1).reset_index(drop=True)
    
    return shuffledDf

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

    # Adding a column 'word_count' with the word count of the text in the column 'text'
    data['word_count'] = data['text'].apply(countWords)

    # Filtering out rows with more than 250 words
    data = data[data['word_count'] <= 350]

    # Selecting important columns
    data = data[['title', 'text', 'offering_id', 'num_helpful_votes', 'overall']]
    print(data)

    # Showing the initial data distribution after the language filtering
    showDataDistribution(data,'overall','Initial data distribution')

    data = distributeDataFive(data)
    
    print(data)

    # Showing the new data distribution after the distribution of data
    showDataDistribution(data,'overall','New data distribution')  

    # Importing hotels data
    pathHotelData = os.getenv('HOTEL_DATA_PATH')
    hotelData = pd.read_csv(pathHotelData)
    hotelData = hotelData[['id', 'hotel_class', 'name', 'address']]

    # Merging filterdData and hotelData
    data = data.merge(hotelData, left_on='offering_id', right_on='id')

    # Replacing None values in the column 'hotel_class' with 0
    data['hotel_class'] = data['hotel_class'].fillna(0)

    # Selecting important columns
    data = data[['title', 'text', 'overall', 'num_helpful_votes', 'name','hotel_class', 'address']]
    print(data)

    # Generating a csv file of new data without index numbers
    pathFilteredData = os.getenv('FILTERED_DATA_PATH')
    data.to_csv(pathFilteredData, index=False)