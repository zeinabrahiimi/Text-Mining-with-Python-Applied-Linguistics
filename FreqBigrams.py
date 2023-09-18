import nltk, re, string, collections
from nltk.util import ngrams  # function for making ngrams
import re

# Reading the'BROWN.txt' file
f = open('BROWN.txt', 'r')
rawtext = f.read()
f.close()

# Preprocessing steps
punctuationNoPeriod = "[" + re.sub("\.", "", string.punctuation) + "]"
text = re.sub(punctuationNoPeriod, "", rawtext)  # Remove punctuation (except periods!)
text = re.sub(r'\d+', '', text)           # Remove numbers
text = re.sub(r'[^\w\s]', '', text)       # Remove additional punctuation

# Tokenizing the text into individual words
tokenized = text.split()

# Converting the text to lowercase and remove stopwords
from nltk.corpus import stopwords
sw = stopwords.words('english')
without_sw = [w for w in tokenized if w.lower() not in sw and w.lower() not in ['would', 'could', 'should', 'might']]

# Calculating bigrams (pairs of words)
esBigrams = ngrams(without_sw, 2)

# Getting the frequency of each bigram in the corpus
esBigramFreq = collections.Counter(esBigrams)

# Getting the 100 most frequent bigrams excluding specific words
most_freq_bigrams = [(bigram, freq) for bigram, freq in esBigramFreq.items() if
                     len(bigram[0]) > 1 and len(bigram[1]) > 1 and
                     bigram[0] not in ['would', 'could', 'should', 'might'] and
                     bigram[1] not in ['would', 'could', 'should', 'might']]

# Getting the 100 most frequent bigrams
most_freq_bigrams = sorted(most_freq_bigrams, key=lambda x: x[1], reverse=True)[:100]
print(most_freq_bigrams)

import pandas as pd

# Creating a pandas DataFrame from the list of bigrams
df = pd.DataFrame(most_freq_bigrams, columns=['Bigram', 'Frequency'])

# Exporting the DataFrame to an Excel file
df.to_excel('most_frequent_bigrams_BROWN.xlsx', index=False)




