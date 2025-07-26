import math
import lmdb
import pickle
#import time
#start_time = time.time()
#Loading vocabulary and document length for BM25
with open("document_lengths.bin", "rb") as file:
    document_lengths = dict(pickle.load(file))
with open("vocabulary.bin", "rb") as file:
    vocabulary = set(pickle.load(file))

results = []
inverted_index = {}
#average document for BM25
avg_journal_lengths = sum(document_lengths.values()) / len(document_lengths)

search_term = input()
#search_term = "financial and new york"

#lower casing and breaking down each search terms
search_terms = [term.lower() for term in search_term.split() if term.lower() in vocabulary]

#loading inverted index for only search terms
env = lmdb.open("InvertedIndex.lmdb")
with env.begin() as txn:
    for term in search_terms:
        serialized = txn.get(str(term).encode('utf-8'))
        if serialized is not None:
            inverted_index[term] = pickle.loads(serialized)

relevant_docs = set()
for term in search_terms:
    if term in inverted_index:
        relevant_docs.update(inverted_index[term].keys())

#constants for the BM25
k1 = 1.5
b = 0.75
#IDF values for each search terms
idf = {}
for term in search_terms:
    if term in inverted_index:
        idf[term] = math.log(len(document_lengths) / (1 + len(inverted_index[term])))

for docno in relevant_docs:
    score = 0.0
    document_length = document_lengths[docno]
    #BM25 ratio denominator
    ratio = (1 - b + b * (document_length / avg_journal_lengths))
    for term in search_terms:
        if term in inverted_index and docno in inverted_index[term]:
            tf = inverted_index[term][docno]
            #BM25 calculation:
            numerator = tf*(k1 + 1)
            denominator = tf + k1 * ratio
            score += idf[term] * (numerator / denominator)
    results.append((docno, score))

results.sort(key=lambda x: x[1], reverse=True)

# to save time making an output string to make only  one call to print function.
output = '\n'.join(f'{docno} {score}' for docno, score in results)
print(output)

#end_time = time.time()
#print(end_time - start_time)
