import nltk, re, string, collections
from nltk.util import ngrams  # function for making ngrams
import re

# Open and read the 'BROWN.txt' file
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

# Convert the text to lowercase and remove stopwords
from nltk.corpus import stopwords
sw = stopwords.words('english')
without_sw = [w for w in tokenized if w.lower() not in sw and w.lower() not in ['would', 'could', 'should', 'might']]

# Calculate trigrams (groups of three words)
esTrigrams = ngrams(without_sw, 3)

# Get the frequency of each trigram in the corpus
esTrigramFreq = collections.Counter(esTrigrams)

# Get the 100 most frequent trigrams excluding specific words
most_freq_trigrams = [(trigram, freq) for trigram, freq in esTrigramFreq.items() if
                      len(trigram[0]) > 1 and len(trigram[1]) > 1 and len(trigram[2]) > 1 and
                      trigram[0] not in ['would', 'could', 'should', 'might'] and
                      trigram[1] not in ['would', 'could', 'should', 'might'] and
                      trigram[2] not in ['would', 'could', 'should', 'might']]

# Get the 100 most frequent trigrams
most_freq_trigrams = sorted(most_freq_trigrams, key=lambda x: x[1], reverse=True)[:80]
print(most_freq_trigrams)

import pandas as pd

# Create a pandas DataFrame from the list of trigrams
df = pd.DataFrame(most_freq_trigrams, columns=['Trigram', 'Frequency'])

# Export the DataFrame to an Excel file
df.to_excel('most_frequent_trigrams_BROWN.xlsx', index=False)




