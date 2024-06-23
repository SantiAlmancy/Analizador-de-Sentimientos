import nltk
from nltk.corpus import stopwords

nltk.download('punkt')
nltk.download('stopwords')

# Create stop words list
stopWords = stopwords.words('english')
## Remove 'not' and 'no' from the stop words list since they have value in context
stopWords.remove('not')
stopWords.remove('no')

def removeStopWords(sentence):
  # Tokenize
  tokens = nltk.word_tokenize(sentence)
  # Filter stop words
  filtered_tokens = [token for token in tokens if token.lower() not in stopWords]

  processed_text = ' '.join(filtered_tokens)
  return processed_text
