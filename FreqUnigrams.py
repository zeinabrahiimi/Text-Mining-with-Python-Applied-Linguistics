import nltk, re, string, collections
from nltk.util import ngrams  # function for making ngrams
import re

# Reading the 'BROWN.txt' file
f = open('BROWN.txt', 'r')
rawtext = f.read()
f.close()

# Preprocessing steps
punctuationNoPeriod = "[" + re.sub("\.", "", string.punctuation) + "]"
text = re.sub(punctuationNoPeriod, "", rawtext)  # Remove punctuation (except periods!)
text = re.sub(r'\d+', '', text)           # Remove numbers
text = re.sub(r'[^\w\s]', '', text)       # Remove additional punctuation

# Tokenize the text into individual words
tokenized = text.split()

# Converting the text to lowercase and remove stopwords
from nltk.corpus import stopwords
sw = stopwords.words('english')
without_sw = [w for w in tokenized if w.lower() not in sw and w.lower() not in ['would', 'could', 'should', 'might']]

# Calculating unigrams (single words)
esUnigrams = ngrams(without_sw, 1)

# Getting the frequency of each unigram in the corpus
esUnigramFreq = collections.Counter(esUnigrams)

# Get the 100 most frequent unigrams excluding specific words
most_freq_unigrams = [(unigram, freq) for unigram, freq in esUnigramFreq.items() if
                      len(unigram[0]) > 1]

# Getting the 100 most frequent unigrams
most_freq_unigrams = sorted(most_freq_unigrams, key=lambda x: x[1], reverse=True)[:100]
print(most_freq_unigrams)

import pandas as pd

# Creating a pandas DataFrame from the list of unigrams
df = pd.DataFrame(most_freq_unigrams, columns=['Unigram', 'Frequency'])

# Exporting the DataFrame to an Excel file
df.to_excel('most_frequent_unigrams_BROWN.xlsx', index=False)




