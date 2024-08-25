'''This file creates idf scores for words parsed from popular Wikipedia pages'''
import os
from sklearn.feature_extraction.text import TfidfVectorizer

doc_corpus = []
num_docs = 0
pages_directory = "pages"

for filename in os.listdir(pages_directory): # opening all files in pages folder
    filepath = os.path.join(pages_directory, filename)
    with open(filepath, 'r', encoding='utf-8') as file:
        content = file.read()
        doc_corpus.append(content) # adding file to document corpus

vectorizer = TfidfVectorizer(use_idf=True)
vectorizer.fit(doc_corpus) # calculating idf scores

idf_scores = vectorizer.idf_
words = vectorizer.get_feature_names_out() 

idf_dict = dict(zip(words,idf_scores)) # creating dictionary of words and matching idf scores

with open("idf_dict.txt", "w", encoding='utf-8') as file:
    for word, score in idf_dict.items():
        file.write(f'{word} {score}\n') # writing out idf dictionary to file
