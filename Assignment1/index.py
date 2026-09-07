#-------------------------------------------------------------------------
# AUTHOR: Diego Mejia
# FILENAME: index.py
# SPECIFICATION: description of the program
# FOR: CS 4250 - Assignment #1
# TIME SPENT: 3 hrs (whole assignment)
#-------------------------------------------------------------------------

# Importing Python libraries
import pandas as pd

# Reading the document collection
data = pd.read_csv("collection.csv")

# Defining the dictionary used for lemmatization
lemmas = {
    "increases": "increase",
    "rising": "rise",
    "increasing": "increase",
    "sales": "sale",
    "homes": "home"
}

# Creating the data structure that will store the inverted index
invertedIndex = {}

# Processing each document in the collection
for i, row in data.iterrows():
    docID = row["Document"]
    text = row["Text"]
# Applying surface-level normalization
    text = text.lower().strip('.,')
# Tokenizing the document
    words = text.split()
# Applying lemmatization
    words = [lemmas.get(word, word) for word in words]
# Building the inverted index
    for word in words:
        if word not in invertedIndex:
            invertedIndex[word] = []
        if docID not in invertedIndex[word]:
            invertedIndex[word].append(docID)
# Printing the inverted index with terms ordered alphabetically
# Expected format:
# term1 : ['Doc1', 'Doc2']
# term2 : ['Doc3']

print("\nInverted Index:\n")
for word in sorted(invertedIndex.keys()):
    print(f"{word}: {invertedIndex[word]}")
print()