from collections import defaultdict
import pickle
import lmdb

#load the prepared file for indexer.
with open('for_indexer.bin', 'rb') as file:
    documents = pickle.load(file)
inverted_index = defaultdict(dict)
document_lengths = {}
vocabulary = set()

for docno, words in documents:
    ##length of each journal
    document_lengths[docno] = len(words)
    term_frequency = defaultdict(int)
    for word in words:
        ##frequency of word in journal
        term_frequency[word] += 1
    vocabulary.update(term_frequency.keys())
    for term, frequency in term_frequency.items():
        ##Inverted index with frequency
        inverted_index[term][docno] = frequency

with open("vocabulary.bin", "wb") as file:
    pickle.dump(vocabulary, file)
with open("document_lengths.bin", "wb") as file:
    pickle.dump(document_lengths, file)

env = lmdb.open("InvertedIndex.lmdb", map_size=2147483649)
with env.begin(write=True) as txn:
    for key, value in inverted_index.items():
        txn.put(str(key).encode('utf-8'), pickle.dumps(value))
env.close()
