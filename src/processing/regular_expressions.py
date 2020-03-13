#!/usr/bin/env python

"""http://nlp.stanford.edu/projects/glove/preprocess-twitter.rb contains regular expression in ruby.
Translation of Ruby script with little variations to create features for text classification"""
import re

FLAGS = re.MULTILINE | re.DOTALL
#ADD TWEETS AS OTHER FEATURES
def hashtag(text):
    text = text.group()
    hashtag_body = text[1:]
    if hashtag_body.isupper():
        result = " {} ".format(hashtag_body.lower())
    else:
        result = " ".join([" "] + [re.sub(r"([A-Z])",r" \1 ", hashtag_body, flags=FLAGS)])
    return " "+result+" "

def allcaps(text):
    text = text.group()
    return text.lower() + " <allcaps> "

def apostrophe(text):
	text = text.group()
	return text.replace("'","")

def tweet_preprocessing(text):
# eyes and nose sets for smiley faces
    eyes = r"[8xX:=;]"
    nose = r"['`-]?"
    phone_number =  r"((\+\d{1,3}[\-\s.]*)?\d{3}[-\.\s]?\d{3}[-\.\s]?\d{4}|(\+\d{1,2}[\-\s.]*)?\(\d{3}\)\s*\d{3}[-\.\s]?\d{4}|\d{3}[-\.\s]?\d{4})"


    # function so code less repetitive
    def re_sub(pattern, repl):
        return re.sub(pattern, repl, text, flags=FLAGS)
    text = re_sub(r"\w+'s", apostrophe)
    text = re_sub(phone_number," <number> ")
    text = re_sub(r"https?:\/\/\S+\b|www\.(\w+\.)+\S*", " <url> ") 
    text = re_sub(r"@\w+", " <user> ")
    text = re_sub(r"{}{}[)dD3]+|[(]+{}{}".format(eyes, nose, nose, eyes), " <smile> ") 
    text = re_sub(r"{}{}p+".format(eyes, nose), " <lolface> ")
    text = re_sub(r"{}{}\(+|[)Dd]+{}{}".format(eyes, nose, nose, eyes), " <sadface> ")
    text = re_sub(r"{}{}[\/|l*]".format(eyes, nose), " <neutralface> ")
    text = re_sub(r"/"," / ")
    text = re_sub(r"<3"," <heart> ")
    text = re_sub(r"[-+]?[.\d]*[\d]+[:,.\d]*", " <number> ")
    text = re_sub(r"#\S+", " ")
    #text = re_sub(r"[-_]"," ")
    text = re_sub(r"([!?.]){2,}", r"\1 <repeat> ")
    #text = re_sub(r"\b(\S*?)(.)\2{2,}\b", r"\1\2 <elong>")
    text = re_sub(r"\[.+\]","")
    text = re_sub(r"(\w*)…",r"\1 ")
    text = re_sub(r"\s+"," ")
    text = re_sub(r"([A-Z]){2,}", allcaps)
   

    return text.lower()
#text =  "RT @ #happyfuncoding: this is a typical Twitter tweet :-)"
#text = "HTML entities & other Web oddities can be an áacute pain >:("
#text = r"""phone                                   numbers              are        like 
#+1 (800) 123-4567, 
#+91 (800) 123-4567, and              #+642 745 741 7457  123-4567     123-456            """
#matches \n too
text = "\n#Joke: what do you… … call a pig with three eyes???piiig!!!ALLCAPS ....[Google \n \n documentation][dbr5324195678!@#$%^&()_+';'] 3 2"
#text = "I TEST alllll kinds of #hashtags and #HASHTAGS and ( : )':  ))):  ;) XD xD Dx DX ) haaaaappppyyy (: :( and  +40 4:45 #HashTags,words/random/random/ USA @mentions and 3000:1 (http://t.co/dkfjkdf). w/ <3 :) haha!!!!! so on...."
tokens = tweet_preprocessing(text)
print(tokens)

