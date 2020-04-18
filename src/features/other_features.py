import nltk
import textblob,re
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer as VS
from pathlib import Path
import os,sys

path = Path(os.path.abspath(__file__)).parent.parent
#print(path)
sys.path.insert(1,os.path.join(path))

from processing.emojis import extract_emoji

# nltk.download('punkt')
# nltk.download('averaged_perceptron_tagger')

stopwords = ['the','to','and','is','my','just','us','its','it','up','in','for','of','at','this','on','am','that','be','with','are','me','it','all','like','so','do','rt','ff','you','your','if','as','or','an','a','i','f','s','it','day','but','have','about',"we","after","who","what","day","when","such","how","by","been","she","he","their","wa","today","from","then","me","via","only","off","now","let","our","by","new","many","only","there","here","him","her","today","one","has","d","s","h","a","o","f","e","r","y","u"]

pos_family = {
    'noun' : ['NN','NNS','NNP','NNPS'],
    'pron' : ['PRP','PRP$','WP','WP$'],
    'verb' : ['VB','VBD','VBG','VBN','VBP','VBZ'],
    'adj' :  ['JJ','JJR','JJS'],
    'adv' : ['RB','RBR','RBS','WRB']
}

def get_postag_count(text, tag):
	text = re.sub(r"[^A-Za-z|(!?) ]","",text)
	count = 0
	try:
		blob = textblob.TextBlob(text)
		for tup in blob.tags:
			pos = list(tup)[1]
			if pos in pos_family[tag]:
				count += 1
	except:
		pass
	return count

def get_vader_sentiment(text):
	sentiment_analyzer = VS()
	sentiment = sentiment_analyzer.polarity_scores(text)
	return [sentiment['neg'], sentiment['pos'], sentiment['neu'], sentiment['compound']]

def count_stop_words(text):
    count=0
    text = text.lower()
    for word in text.split():
        if word in stopwords:
            count+=1
    return count

def get_text_features(text):
	num_exclamation_marks =text.count('!')
	num_question_marks = text.count('?')
	num_symbols = sum([text.count(w) for w in '*&$%'])
	stopword_count = count_stop_words(text)
	emoji_count = len(extract_emoji(text))
	return [num_exclamation_marks,num_question_marks,num_symbols,stopword_count,emoji_count]

def get_twitter_features(text):
	hashtag = text.count('hashtag')
	user = text.count("user")
	allcaps = text.count("allcaps")
	text = re.sub(r"(hashtag|user|allcaps)"," ", text)
	text = text.strip()
	text = re.sub(r"\s+"," ",text)
	return [text,hashtag,user,allcaps]

def other_text_features(text):
	total_length = len(text)
	num_words =  len(text.split())
	num_unique_words = len(set([w for w in text.split()]))
	words_vs_unique = num_unique_words / num_words
	return [total_length,num_words,num_unique_words,words_vs_unique]
#print(get_text_features("kg😀 😁 😂 🤣 😃 😄 😅 😆 😉 "))
