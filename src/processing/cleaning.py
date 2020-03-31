import pandas as pd
from tqdm.auto import tqdm
tqdm.pandas()

from special_char import clean_special_chars
from html_tag_remover import strip_tags
from emojis import remove_duplicates
from spellings import replace_elongated_text
from contractions import clean_contractions,replace_slang
from regular_expressions import tweet_preprocessing

def remove_empty(dataframe):
    drop_rows = dataframe[dataframe['tweet']==""]
    dataframe.drop(drop_rows.index, axis=0,inplace=True)
    return dataframe

def clean_data(path,embeddings=False):
    #add_lower()
    dataframe = pd.read_csv(path)
    if not embeddings:
        return dataframe
    else:
        dataframe["tweet"] = dataframe['tweet'].progress_apply(lambda x: replace_slang(x))
        dataframe['tweet'] = dataframe['tweet'].progress_apply(lambda x : strip_tags(x))
        dataframe['tweet'] = dataframe['tweet'].progress_apply(lambda x: tweet_preprocessing(x))
        dataframe["tweet"] = dataframe["tweet"].progress_apply(lambda x : x.lower())
        dataframe['tweet'] = dataframe['tweet'].progress_apply(lambda x: clean_contractions(x))
        dataframe = remove_empty(dataframe)
        dataframe['tweet'] = dataframe['tweet'].progress_apply(lambda x: replace_elongated_text(x))
        #dataframe['tweet'] = dataframe['tweet'].progress_apply(lambda x: remove_duplicates(x))
        dataframe['tweet'] = dataframe['tweet'].progress_apply(lambda x: clean_special_chars(x))       
    return dataframe
    
    






