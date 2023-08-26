Welcome to the Text Mining with Python for Applied Linguistics project!

#  Project Highlight 
In the realm of Applied Linguistics, text mining proved to be fruitful, especially in L2 Research. 
For example, in this project, I am going to get the most frequent bigrams of different research paradigms, including Quantiative and Qualitative papers.
What we actually did was to get the pattern of language use in these paradigms. Specifically, we can detect which two words occur most frequently in the corpus of Quantitative and Qualitative papers.
## Data Confidentiality 
The dataset (corpora of Quantitative and Qualitative papers) is confidential as it belongs to my dear Linguistics Professor. Therefore, considering  ethical issues of data sharing, I am unable to share the specific data used in this analysis.
## Brown Corpus as a Substitue 
Hence, to ensure data analysis transparency, I have used the Brown corpus, an open-access dataset comprising of a versatile array of text from different resources. This corpus can be used as a substitue to showcase the keyword analysis. 
### Data Preprocessing
The preprocessing step includes removing punctuations and numbers to end up having meaningful content words. 
What is more, I also exclude some extranous words that may not provide meanings (e.g., could, should, would, etc.).
The preprocessing stage is a must as we want to confrom to the GIGO (i.e.,Garbage in, Garbage out) principle. Therefore, we will get clean input to have a clean outpude.
### Data Processing 
Now, we tokenize the text into individual words.
Next, we convert the text to lowercase letters and remove stop words stop words (i.e., function words).
Then, we calculate the n-grams (Unigrams, Bigrams, and Trigrams).
Finally, using the collections.Counter class, we calculate the frequency of n-grams. It is also worth mentioning that we also exclude n-grams based on their lengths. 
### Data Presentation
The selected n-grams, in conjunction with their frequencies, are presented in a pandas DataFrame, which is then exported to an Excel file.
## Conclusion 
Through this project, we showcase the potential of text mining in capturing meaningful insights from textual data. We hope that this work talk fellow researchers into exploring the world of text analysis for enhancing their understanding of Applied Linguistics Research!


