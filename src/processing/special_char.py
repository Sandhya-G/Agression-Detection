#!/usr/bin/env python

import string
from glove_utils import build_vocab
from tqdm import tqdm
import pandas as pd
import sys
import os
from pathlib import Path
sys.path.append(Path("/home/sandhya/Project/"))
#sys.path.insert(1, Path((os.path.abspath(__file__)),"/../..")
#print(os.path.dirname(os.path.abspath(__file__))
import paths

punct = r"/-'?!.,#$%\'()*+-/:;<=>@[\\]^_`{|}~" + r'""“”’' + r'∞θ÷α•à−β∅³π‘₹´°£€\×™√²—–&'

def unknown_punct(embed, punct):
    unknown = ''
    for p in punct:
        if p not in embed:
            unknown += p
            unknown += ' '
    return unknown
#currencies are replaced with `e`
punct_mapping = {"‘": "'", "₹": "e", "´": "'", "°": "", "€": "e", "™": "tm", "√": " sqrt ", "×": "x", "²": "2", "—": "-", "–": "-", "’": "'", "_": "-", "`": "'", '“': '"', '”': '"', '“': '"', "£": "e", '∞': 'infinity', 'θ': 'theta', '÷': '/', 'α': 'alpha', '•': '.', 'à': 'a', '−': '-', 'β': 'beta', '∅': '', '³': '3', 'π': 'pi', }

def clean_special_chars(text, punct, mapping):
    for p in mapping:
        text = text.replace(p, mapping[p])
    
    for p in punct:
        text = text.replace(p, f' {p} ')
    
    specials = {'\u200b': ' ', '…': ' ... ', '\ufeff': ''}  # Other special characters
    for s in specials:
        text = text.replace(s, specials[s])
    
    return text

white_list = string.ascii_letters + string.digits + ' ' +  "'"
#glove_chars = ''.join([c for c in tqdm(glove_embed) if len(c) == 1])
#glove_symbols = ''.join([c for c in glove_chars if not c in white_list])
glove_symbols = '.:,!"?()-/*>^<&_~;|[]`$=+%@\\#}{'
df = pd.read_csv(CONST().TRAIN_DATA)
all_characters = build_vocab(list())
symbols_to_delete = ''.join([c for c in all_characters if not c in white_list if not c in glove_symbols])

remove_dict = {ord(c):f'' for c in symbols_to_delete}

def handle_punctuation(x):
    x = x.translate(remove_dict)
    return x
print("all_characters")