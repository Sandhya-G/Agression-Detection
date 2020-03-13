#!/usr/bin/env python

import string
from glove_utils import build_vocab
from tqdm import tqdm
import pandas as pd
import sys
import os
import re
from pathlib import Path

path = Path(os.path.abspath(__file__)).parent.parent.parent
#print(path)

sys.path.insert(1,os.path.join(path))

#sys.path.insert(1, Path((os.path.abspath(__file__)),"/../..")

import paths

punct = r"/-'?!#$%\'().,*+-/:;=@[\\]^_`{|}~" + r'""“”’' + r'∞θ÷α•à−β∅³π‘₹´°£€\×™√²—–&'

# white_list = string.ascii_letters + string.digits + ' ' +  "'"
#glove_chars = ''.join([c for c in tqdm(glove_embed) if len(c) == 1])
#glove_symbols = ''.join([c for c in glove_chars if not c in white_list])
# glove_symbols = '.:,!"?()-/*>^<&_~;|[]`$=+%@\\#}{'
# df = pd.read_csv(paths.CONST().TRAIN_DATA)
# all_characters = build_vocab(list(df['tweet']))
symbols_to_isolate = '!?&'
symbols_to_delete = ':-"~*=@$;%+(|)^{}\\[]/#.,…ð\x9f\x98â\x9c¨\x92\x87\x80¦👏…\x86\x9d\x93\x99\x8f\x8e\x89¤ï¸😩😂¬\x8a\x90¶¾😭\x9e\x95😅💊👫❤½✌️★\x8d\x8b»\x84\x8c¹👋\x96😳\xad\x82©®👀😏ó\x94😋😌¼✂😻🙌💦😎👌🙅✋🚫🍞💁😪ª\x9a\x91«🙏\x81ã👟\x9b\x88\x97💯¢¥😷¡\x83😕😍😒º💀😢😴\U000feb9f¿👊💸😖🙈¯💩ìíè🆗🆒äçåµñ⊕🙊👅🎵ü😈🍻🎉🎈😊🔫☺👬👭💥§😆♥◡̈⃝😉😜é😫🐸☕😁😱‼💙💃🎤👐🌈🎭😘💍💕🔐✊💋🔪±😹\ue412🐛💰·✈�ëê😐😡👉👈🔴⚫👎😑💜❗👼😔æ→👩👆👯😝🐎\U000feb97\ue411\ue427🏆📝📃🏀🐼💅😤📑😠🐱😶🍟á😃📖û👑👿\U000fe343😥🍇🍼😛🚮💖😺✨🌟💫😞🎂🍰🍑💑💆😣🎄⛄🎅🙋🍁\U000fe35b\U000feb5d\U000fe358\U000feb7b\U000fe334\U000fec11\U000feb9d💎👍💵🚨💧🐢😦🙇🌵👸💞🔥💨🎼🎁🌴☀🙎\U000feb9e💄💗🔑👶🚼☝🎲⃣🐥🐣😾。🚌🙆💏🚶\U000fe32c🎶🎧🙉😿øù💡🍅😟🐷📰😓🐊💪😮🇺🇸\U000fe326❓⭐🍍ö😵🐦🐝🐯🍃🌿\ue31f\ue301📕📚🏡😬🙀ò💤😨👄🎬🎥\U000feba0💛🌙☁🌠🆚👻🏈😗😄\U000fe346\U000feb0f💚🎊\U000fe33a⚡👮💲📢⛽⚾🍂🚙\U000fe327👇🚕⚪\ue40d\ue04f\ue40c\ue107🐙🍄✔💣🍆😲🕛′🍗♿🇬🇧😧🏄🍪❄🌀📣👰\ue108👧💢🇮🇹✖\U000feb5b\U000fe321🍺👷🌝🏃🎯👂🐬🐐\U000fe194\U000fe355❌⭕🌹👞🙍˘🐤👠👛💳🍉😽⬇🏂😰👺🚧🗿🌊🏊😇î♨🔊🍕ú♫\U000fe511\U000fe4e4\U000fe4dd🌾🔚\ue41f🐠❕🚬🍸\U000fe190♡❔\U000fe4f5🌸🚓🚒💺🍖🍝🍤🍛📷💔👹😚\U000fe320💓💇👵💉🐈🐶😼🚀⌚💂💭🍫🐒\U000fe351\U000fe335😯👲🚘🚩🌽💘📋\U000fe340🌳\U000fe825\U000feb99\U000fe347🍵🚥🏰\ue40e\ue24d\ue337👽🔓\U000feb5c🅰🐺📼🐍łę⏳🐂，\ue420🍩👙📉🌚'
remove_dict = {ord(c):f'' for c in symbols_to_delete}
isolate_dict = {ord(c):f' {c} ' for c in symbols_to_isolate}


    
#remove_dict = {ord(c):f'' for c in symbols_to_delete}




#currencies are replaced with `e`
#2 and 3 for the squares and cubes might a well you regex
punct_mapping = {"‘": "'","₹": "e", "´": "'", "°": "", "€": "e", "™": "tm", "√": " sqrt ", "×": "x", "²": "2", "—": "-", "–": "-", "’": "'", "_": "-", "`": "'", '“': '"', '”': '"', '“': '"', "£": "e", '∞': 'infinity', 'θ': 'theta', '÷': '/', 'α': 'alpha', '•': '.', 'à': 'a', '−': '-', 'β': 'beta', '∅': '', '³': '3', 'π': 'pi', }

def clean_special_chars(text, punct=punct, mapping=punct_mapping,delete_symbols=symbols_to_delete):
    for p in mapping:
    	text = text.replace(p, mapping[p])
    
    specials = {'\u200b': ' ', '…': ' ... '}  # Other special characters that I have to deal with in last
    for s in specials:
        text = text.replace(s, specials[s])
    text =text.translate(remove_dict)
    text = text.translate(isolate_dict)
    re.sub(r"[.]*\d+","<number",text)
    return text

print(clean_special_chars("dfvf₹ ffv₹😂 rfvf₹ s😂d😂v ₹₹₹.....",punct,punct_mapping,symbols_to_delete))
