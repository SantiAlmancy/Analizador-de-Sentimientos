import nltk
from nltk.corpus import wordnet
from nltk.stem import WordNetLemmatizer
nltk.download('wordnet')
nltk.download('averaged_perceptron_tagger')

# Pos Tag Finder function
def posTagFinder(nltkTag):
    if nltkTag.startswith('J'):
        return wordnet.ADJ
    elif nltkTag.startswith('V'):
        return wordnet.VERB
    elif nltkTag.startswith('N'):
        return wordnet.NOUN
    elif nltkTag.startswith('R'):
        return wordnet.ADV
    else:
        return None
  
# Lemmatization Process
def lemmatizer(sentence):
  ## Getting pos tags
  posTags = nltk.pos_tag(nltk.word_tokenize(sentence))
  wordnetTagged = list(map(lambda x: (x[0], posTagFinder(x[1])), posTags))
  ## Lemmatization
  lemmatizer = WordNetLemmatizer()
  lemmatizedSentence = []
  for word, tag in wordnetTagged:
      if tag is None:
          lemmatizedSentence.append(word) # Avoid tagging unnecesary words
      else:
          lemmatizedSentence.append(lemmatizer.lemmatize(word, tag)) # Adding tag to lemmatize
  lemmatizedSentence = " ".join(lemmatizedSentence)
  return lemmatizedSentence
