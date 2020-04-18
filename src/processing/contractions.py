import re
contraction_mapping = {"ain't": "is not", "aren't": "are not","can't": "cannot", "cause": "because", "could've": "could have", "couldn't": "could not", "didn't": "did not",  "doesn't": "does not", "don't": "do not", "hadn't": "had not", "hasn't": "has not", "haven't": "have not", "he'd": "he would","he'll": "he will", "he's": "he is", "how'd": "how did", "how'd'y": "how do you", "how'll": "how will", "how's": "how is",  "I'd": "I would", "I'd've": "I would have", "I'll": "I will", "I'll've": "I will have","I'm": "I am", "I've": "I have", "i'd": "i would", "i'd've": "i would have", "i'll": "i will",  "i'll've": "i will have","i'm": "i am", "i've": "i have", "isn't": "is not", "it'd": "it would", "it'd've": "it would have", "it'll": "it will", "it'll've": "it will have","it's": "it is", "let's": "let us", "ma'am": "madam", "mayn't": "may not", "might've": "might have","mightn't": "might not","mightn't've": "might not have", "must've": "must have", "mustn't": "must not", "mustn't've": "must not have", "needn't": "need not", "needn't've": "need not have","o'clock": "of the clock", "oughtn't": "ought not", "oughtn't've": "ought not have", "shan't": "shall not", "sha'n't": "shall not", "shan't've": "shall not have", "she'd": "she would", "she'd've": "she would have", "she'll": "she will", "she'll've": "she will have", "she's": "she is", "should've": "should have", "shouldn't": "should not", "shouldn't've": "should not have", "so've": "so have","so's": "so as", "this's": "this is","that'd": "that would", "that'd've": "that would have", "that's": "that is", "there'd": "there would", "there'd've": "there would have", "there's": "there is", "here's": "here is","they'd": "they would", "they'd've": "they would have", "they'll": "they will", "they'll've": "they will have", "they're": "they are", "they've": "they have", "to've": "to have", "wasn't": "was not", "we'd": "we would", "we'd've": "we would have", "we'll": "we will", "we'll've": "we will have", "we're": "we are", "we've": "we have", "weren't": "were not", "what'll": "what will", "what'll've": "what will have", "what're": "what are",  "what's": "what is", "what've": "what have", "when's": "when is", "when've": "when have", "where'd": "where did", "where's": "where is", "where've": "where have", "who'll": "who will", "who'll've": "who will have", "who's": "who is", "who've": "who have", "why's": "why is", "why've": "why have", "will've": "will have", "won't": "will not", "won't've": "will not have", "would've": "would have", "wouldn't": "would not", "wouldn't've": "would not have", "y'all": "you all", "y'all'd": "you all would","y'all'd've": "you all would have","y'all're": "you all are","y'all've": "you all have","you'd": "you would", "you'd've": "you would have", "you'll": "you will", "you'll've": "you will have", "you're": "you are", "you've": "you have","RT":"","rt":" ","…":"","y'all":"you all","yall":"you all","ho":"hoe","aint":"is not"}
 

def clean_contractions(text, mapping=contraction_mapping):
    specials = ["’", "‘", "´", "`"]
    for s in specials:
        text = text.replace(s, "'")
    text = ' '.join([mapping[t.lower()] if t.lower() in mapping else t for t in text.split(" ")])
    #remaining 
    text = re.sub(r"\'re", " are", text)
    text = re.sub(r"\'d", " would", text)
    text = re.sub(r"\'ll", " will", text)
    text = re.sub(r"\'t", " not", text)
    text = re.sub(r"\'ve", " have", text)
    text = re.sub(r"\'m", " am", text)
    return text
slang_dict = {"AFAIK":"As Far As I Know",
"AFK":"Away From Keyboard",
"ASAP":"As Soon As Possible",
"ATK":"At The Keyboard",
"ATM":"At The Moment",
"A3":"Anytime, Anywhere, Anyplace",
"BAK":"Back At Keyboard",
"BBL":"Be Back Later",
"BBS":"Be Back Soon",
"BFN":"Bye For Now",
"B4N":"Bye For Now",
"BRB":"Be Right Back",
"BRT":"Be Right There",
"BTW":"By The Way",
"B4":"Before",
"B4N":"Bye For Now",
"CU":"See You",
"CUL8R":"See You Later",
"CYA":"See You",
"FAQ":"Frequently Asked Questions",
"FC":"Fingers Crossed",
"FWIW":"For What It's Worth",
"FYI":"For Your Information",
"GAL":"Get A Life",
"GG":"Good Game",
"GN":"Good Night",
"GMTA":"Great Minds Think Alike",
"GR8":"Great!",
"G9":"Genius",
"IC":"I See",
"ICQ":"I Seek you",
"ILU": "I Love You",
"IMHO":"In My Honest/Humble Opinion",
"IMO":"In My Opinion",
"IOW":"In Other Words",
"IRL":"In Real Life",
"IKR":"I Know Right",
"KISS":"Keep It Simple, Stupid",
"LDR":"Long Distance Relationship",
"LMAO":"Laugh My Ass Off",
"LOL":"Laughing Out Loud",
"LTNS":"Long Time No See",
"L8R":"Later",
"MTE":"My Thoughts Exactly",
"M8":"Mate",
"NRN":"No Reply Necessary",
"OIC":"Oh I See",
"PITA":"Pain In The Ass",
"PRT":"Party",
"PRW":"Parents Are Watching",
"ROFL":"Rolling On The Floor Laughing",
"ROFLOL":"Rolling On The Floor Laughing Out Loud",
"ROTFLMAO":"Rolling On The Floor Laughing My A.. Off",
"SK8":"Skate",
"ASL":"Age, Sex, Location",
"THX":"Thank You",
"TTFN":"Goodbye For Now!",
"TTYL":"Talk To You Later",
"U":"You",
"U2":"You Too",
"U4E":"Yours For Ever",
"WB":"Welcome Back",
"WTF":"What The Fuck",
"WTG":"Way To Go!",
"WUF":"Where Are You From?",
"W8":"Wait"}
lower_slang_dict = {key.lower(): value.lower() for key, value in slang_dict.items()}
def replace_slang(text,mapping=lower_slang_dict):
     return ' '.join([mapping[t.lower()] if t.lower() in mapping else t for t in text.split(" ")])

print(replace_slang("TTYL W8"))
