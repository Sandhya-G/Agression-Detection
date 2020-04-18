import re
from special_char import clean_special_chars
from html_tag_remover import strip_tags
from emojis import remove_duplicates,replace_emojis_with_text,remove_emoji
from spellings import replace_elongated_text
from contractions import clean_contractions,replace_slang
from regular_expressions import tweet_preprocessing

stopwords = ['the','to','and','is','my','just','us','its','it','up','in','for','of','at','this','on','am','that','be','with','are','me','it','all','like','so','do','rt','ff','you','your','if','as','or','an','a','i','f','s','it','day','but','have','about',"we","after","who","what","day","when","such","how","by","been","she","he","their","wa","today","from","then","me","via","only","off","now","let","our","by","new","many","only","there","here","him","her","today","one","has","d","s","h","a","o","f","e","r","y","u"]

def clean_text(text,embeddings=False,remove_emojis=True,replace_emojis=False,stopword=True,lem=False):
    text = replace_slang(text)
    text = strip_tags(text)
    text = clean_contractions(text)
    text = tweet_preprocessing(text,embedding=embeddings)
    text = replace_elongated_text(text)
    text = clean_special_chars(text,embedding=embeddings) 
    if stopword:
        text = ' '.join([word for word in text.split() if word.lower() not in (stopwords)])
    text = text.strip()
    text = re.sub(r"\s+"," ",text)
    if len(text)>0 and replace_emojis:
        text = replace_emojis_with_text(text)
    elif len(text)>0 and remove_emojis:
        text = remove_emoji(text)  
    text = text.strip()
    text = re.sub(r"\s+"," ",text) 
    if len(text)>0:  
        return text
    
    






