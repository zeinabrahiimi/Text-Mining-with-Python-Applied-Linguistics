import spacy
import pandas as pd

nlp = spacy.load("en_core_web_sm")
with open("text2.txt", "r") as f:
    text = f.read()
print(text)

# Creating a Doc container:
doc = nlp(text)

for token in doc[:11]:
    print(token)


# To access the sentences in the Doc container, we can use the attribute sents.
for sent in doc.sents:
    print(sent)
print("finish")


sent1 = list(doc.sents)[0]
print(sent1)
print("done")


# Part-Of-Speech, Syntactic Dependency, Morphological analysis
linguistic_data = []  # Create an empty list to store the data

for token in sent1[1:17]:
    linguistic_data.append([token.text, token.pos_, token.dep_, token.morph])

# Create a DataFrame from the linguistic_data list
df_linguistic_data = pd.DataFrame(linguistic_data, columns=["Token", "POS", "Dependency", "Morphology"])

# Store the DataFrame in a CSV file
df_linguistic_data.to_csv("linguistic_data.csv", index=False)
print("dataframe for linguistic data was saved in a csv file! ")


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



