import spacy
import pandas as pd


# Loading the small English language model
nlp = spacy.load("en_core_web_sm")

# Reading the content of your txt file.
with open("text2.txt", "r") as f:
    text = f.read()
print(text)

# Creating a Doc container:
doc = nlp(text)

# Print the first sentence.
sent1 = list(doc.sents)[0]
print(sent1)
print("done")

# Creating an empty list to store linguistic  (i.e., Part-Of-Speech, Syntactic Dependency, Morphological analysis)
linguistic_data = []  # Create an empty list to store the data

# Extracting linguistic info. for the specific tokens
for token in sent1[1:17]:
    linguistic_data.append([token.text, token.pos_, token.dep_, token.morph])

# Creating a DataFrame from the linguistic_data list
df_linguistic_data = pd.DataFrame(linguistic_data, columns=["Token", "POS", "Dependency", "Morphology"])

# Saving the DataFrame to a CSV file
df_linguistic_data.to_csv("linguistic_data.csv", index=False)
print(" The dataframe for linguistic data was saved in a csv file! ")


# Each DET det
# part NOUN nsubj Number=Sing
# of ADP prep
# the DET det Definite=Def|PronType=Art
# life NOUN pobj Number=Sing
# can AUX aux VerbForm=Fin
# be AUX ROOT VerbForm=Inf
# the DET det Definite=Def|PronType=Art
# happiest ADJ amod Degree=Sup
# part NOUN attr Number=Sing
# and CCONJ cc ConjType=Cmp
# it PRON nsubj Case=Nom|Gender=Neut|Number=Sing|Person=3|PronType=Prs
# only ADV advmod
# depends VERB conj Number=Sing|Person=3|Tense=Pres|VerbForm=Fin
# on ADP prep
# ourselves PRON pobj Case=Acc|Number=Plur|Person=1|PronType=Prs|Reflex=Yes



