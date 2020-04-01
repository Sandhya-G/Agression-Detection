from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.feature_selection import SelectKBest
from sklearn.feature_selection import f_classif

def ngram_vectorize(Vectorize,train_texts, train_labels,test_texts,top_k=20000,NGRAM_RANGE = (1, 2),STOPWORDS = None,TOKEN_MODE = 'word',MAX_DOCUMENT_FREQUENCY = 0.75,MIN_DOCUMENT_FREQUENCY = 2):
    """Vectorizes texts as n-gram vectors"""
    # Create keyword arguments to pass to the 'tf-idf' vectorizer.
    kwargs = {
            'ngram_range': NGRAM_RANGE,  # Use 1-grams + 2-grams.
            'strip_accents': 'unicode',
            'decode_error': 'replace',
            'stop_words' : STOPWORDS,
            'analyzer': TOKEN_MODE,  
            'max_df' : MAX_DOCUMENT_FREQUENCY,
            'min_df': MIN_DOCUMENT_FREQUENCY,
    }
    vectorizer = Vectorize(**kwargs)

    # Learn vocabulary from training texts and vectorize training texts.
    x_train = vectorizer.fit_transform(train_texts)

    # Vectorize test texts.
    x_test = vectorizer.transform(test_texts)

    # Select top 'k' of the vectorized features.
    selector = SelectKBest(f_classif, k=min(top_k, x_train.shape[1]))
    selector.fit(x_train, train_labels)
    x_train = selector.transform(x_train).astype('float32')
    x_test = selector.transform(x_test).astype('float32')
    return x_train, x_test

