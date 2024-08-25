from sklearn.feature_extraction.text import TfidfVectorizer
import pandas as pd

# loading in document corpus
doc_corpus = [] 
with open("adzuna_doc_corpus.txt", "r", encoding='utf-8') as file:
    for line in file:
        doc_corpus.append(line.strip())
    
# loading in idf dictionary
idf_dict = dict() 
with open("idf_dict.txt", "r", encoding='utf-8') as file:
    for line in file:
        word = line.split(" ")[0]
        score = line.split(" ")[1]
        idf_dict[word] = float(score)

vectorizer = TfidfVectorizer(use_idf=False, norm=None)
tf_matrix = vectorizer.fit_transform(doc_corpus)
tf_matrix = tf_matrix.toarray()
tf_matrix = tf_matrix.T
doc_idx = list(range(len(doc_corpus)))
words = vectorizer.get_feature_names_out()

df = pd.DataFrame(tf_matrix, columns=doc_idx)
df["average_tf"] = df.mean(axis=1)
df.insert(0,'word',words)
df = df[~df['word'].str.contains(r'\d', regex=True)]
df["word_idf"] = df.apply(lambda x: idf_dict[x["word"]] if x["word"] in idf_dict else 0, axis=1)
df["average_tfidf"] = df.apply(lambda x: idf_dict[x["word"]] * x["average_tf"] if x["word"] in idf_dict else 0, axis=1)
dictionary_words = df[(df["average_tfidf"] > 0) & (df["word_idf"] > 2)].sort_values("average_tfidf",ascending=False)
nondictionary_words = df[df["average_tfidf"] == 0].sort_values("average_tf",ascending=False)
print("Top Dictionary Keywords\n")
print(dictionary_words[["word", "average_tfidf"]].head(10),"\n")
print("Top Non-Dictionary Keywords\n")
print(nondictionary_words [["word", "average_tf"]].head(10))
