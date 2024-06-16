import nltk
from nltk.corpus import wordnet
from nltk.stem import WordNetLemmatizer
nltk.download('wordnet')
nltk.download('averaged_perceptron_tagger')

# Pos Tag Finder function
def pos_tag_finder(nltk_tag):
    if nltk_tag.startswith('J'):
        return wordnet.ADJ
    elif nltk_tag.startswith('V'):
        return wordnet.VERB
    elif nltk_tag.startswith('N'):
        return wordnet.NOUN
    elif nltk_tag.startswith('R'):
        return wordnet.ADV
    else:
        return None
  
# Lemmatization Process
def lemmatizer(sentence):
  ## Getting pos tags
  pos_tags = nltk.pos_tag(nltk.word_tokenize(sentence))
  wordnet_tagged = list(map(lambda x: (x[0], pos_tag_finder(x[1])), pos_tags))
  ## Lemmatization
  lemmatizer = WordNetLemmatizer()
  lemmatized_sentence = []
  for word, tag in wordnet_tagged:
      if tag is None:
          lemmatized_sentence.append(word) # Avoid tagging unnecesary words
      else:
          lemmatized_sentence.append(lemmatizer.lemmatize(word, tag)) # Adding tag to lemmatize
  lemmatized_sentence = " ".join(lemmatized_sentence)
  return lemmatized_sentence
