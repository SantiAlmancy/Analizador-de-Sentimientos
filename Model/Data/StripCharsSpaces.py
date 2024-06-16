import re
import os
import pandas as pd
from dotenv import load_dotenv, dotenv_values 

# (\\b[A-Za-z] \\b|\\b [A-Za-z]\\b):
# - \\b[A-Za-z] \\b: Matches a single alphabetic character [A-Za-z] surrounded by word boundaries \\b (i.e., not preceded or followed by other letters or digits).
# - |: Alternation operator to match either of the patterns separated by it.
# - \\b [A-Za-z]\\b: Matches a single alphabetic character [A-Za-z] preceded or followed by a space \\b and followed or preceded by word boundaries \\b.
# - '': Replace the matched patterns with an empty string, effectively removing them from the text.
def singleCharacterRemoval(sentence):
  sentence = re.sub('(\\b[A-Za-z] \\b|\\b [A-Za-z]\\b)', '', sentence)
  return sentence

# Creates a regex pattern to match any character from charsList, treating them literally.
def specialCharacterRemoval(sentence, charsList):
   regex_pattern = '[' + re.escape(''.join(charsList)) + ']'
   return re.sub(regex_pattern, ' ', sentence)