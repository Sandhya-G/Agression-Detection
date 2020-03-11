#!/usr/bin/env python
import operator
import numpy as np
from tqdm import tqdm

def load_embed(file):
    def get_coefs(word,*arr): 
        return word, np.asarray(arr, dtype='float32')
    
    embeddings_index = dict(get_coefs(*o.split(" ")) for o in open(file, encoding='latin'))
        
    return embeddings_index

def build_vocab(sentences, verbose =  True):
    vocab = {}
    for sentence in tqdm(sentences, disable = (not verbose)):
        for word in sentence:
            try:
                vocab[word] += 1
            except KeyError:
                vocab[word] = 1
    return vocab


def check_coverage(vocab,embeddings_index):
    covered = {}
    oov = {}
    covered_word_count = 0
    oov_word_count = 0
    for word in tqdm(vocab):
        try:
            covered[word] = embeddings_index[word]
            covered_word_count += vocab[word]
        except:

            oov[word] = vocab[word]
            oov_word_count += vocab[word]
            pass

    print('Found embeddings for {:.2%} of vocab'.format(len(covered) / len(vocab)))
    print('Found embeddings for  {:.2%} of all text'.format(covered_word_count / (covered_word_count+ oov_word_count)))
    sorted_x = sorted(oov.items(), key=operator.itemgetter(1))[::-1]

    return sorted_x

def add_lower(embedding, vocab):
    count = 0
    for word in vocab:
        if word in embedding and word.lower() not in embedding:  
            embedding[word.lower()] = embedding[word]
            count += 1
    print(f"Added {count} words to embedding")
