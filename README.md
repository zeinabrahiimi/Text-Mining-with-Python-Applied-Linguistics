Welcome to the Text Mining with Python for Applied Linguistics project!

#  Project Highlight 
In the realm of Applied Linguistics, text mining proved to be fruitful, especially in L2 Research. 
For example, this project aims to get the most frequent n-grams (i.e., unigrams, bigrams, and trigrams) of different research paradigms, including both quantiative and qualitative papers.
The primary objective is to identify language usage patterns within these paradigms by determining the word/words occurring most frequently in the corpus of quantitative and qualitative papers.
## Data Confidentiality 
The dataset is confidential as it is owned by my dear Linguistics Professor. Consequently, given the ethical considerations of data sharing, I am unable to share the specific data used in this analysis.
## Brown Corpus as a Substitue 
Hence, to ensure transparency in data analysis, I have used the Brown corpus, an open-access dataset comprising of a versatile array of text from different resources. This corpus can serve as a substitue to showcase the keyword analysis. 
### Data Preprocessing
The preprocessing step involves removing punctuations and numbers to end up having meaningful content words. 
What is more, some extranous words, without substantial meaning, are excluded (e.g., could, should, would, etc.).
The preprocessing stage is a must as we want to confrom to the GIGO (i.e., Garbage in, Garbage out) principle, ensuring clean input results in a clean output.
### Data Processing 
Now, we tokenize the text into individual words.
Next, we convert the text to lowercase letters and remove stop words stop words (i.e., function words).
Then, we calculate the n-grams (Unigrams, Bigrams, and Trigrams).
Finally, using the collections.Counter class, we calculate the frequency of n-grams. Notably, we also exclude n-grams based on their lengths. 
### Data Presentation
The selected n-grams, in conjunction with their frequencies, are presented in a pandas DataFrame, which is then exported to an Excel file.
## Conclusion 
This project showcases the potential of text mining in capturing informative insights from textual data. We hope that this work talk fellow researchers into exploring the world of text analysis for enhancing their understanding of Applied Linguistics Research!


