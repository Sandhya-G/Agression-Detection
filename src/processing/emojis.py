#!/usr/bin/env python
import re
import emoji
try:
    uchr = unichr  # Python 2
    import sys
    if sys.maxunicode == 0xffff:
        # narrow build, define alternative unichr encoding to surrogate pairs
        # as unichr(sys.maxunicode + 1) fails.
        def uchr(codepoint):
            return (
                unichr(codepoint) if codepoint <= sys.maxunicode else
                unichr(codepoint - 0x010000 >> 10 | 0xD800) +
                unichr(codepoint & 0x3FF | 0xDC00)
            )
except NameError:
    uchr = chr  # Python 3

# Unicode 11.0 Emoji Component map (deemed safe to remove)
_removable_emoji_components = (
    (0x20E3, 0xFE0F),             # combining enclosing keycap, VARIATION SELECTOR-16
    range(0x1F1E6, 0x1F1FF + 1),  # regional indicator symbol letter a..regional indicator symbol letter z
    range(0x1F3FB, 0x1F3FF + 1),  # light skin tone..dark skin tone
    range(0x1F9B0, 0x1F9B3 + 1),  # red-haired..white-haired
    range(0xE0020, 0xE007F + 1),  # tag space..cancel tag
)
emoji_components = re.compile(u'({})'.format(u'|'.join([
    re.escape(uchr(c)) for r in _removable_emoji_components for c in r])),
    flags=re.UNICODE)

def remove_emoji(text, remove_components=False):
    cleaned = emoji.get_emoji_regexp().sub(u'', text)
    if remove_components:
        cleaned = emoji_components.sub(u'', cleaned)
    return cleaned

def is_emoji(char):
    assert isinstance(char,str) and len(char)==1,"This function  only accepts single characters"
    return char in emoji.UNICODE_EMOJI
def get_emoji_name(char):
    if(is_emoji(char)):
        return emoji.UNICODE_EMOJI[char]
def extract_emoji(char):
  return ''.join(c for c in char if c in emoji.UNICODE_EMOJI)

#also removes emoji if it repeats itself for example "AABBACCDB" --> "ABACDB"
def replace_emojis_with_text(text):
    assert isinstance(text,str) and len(text)>0,"size must be greater than 0" 
    replaced_text = get_emoji_name(text[0])[1:-1]+" " if(is_emoji(text[0])) else text[0]

    for i in range(1,len(text)) :
        char = text[i]
        previous_char = text[i-1]
        if(get_emoji_name(char) is None):
            replaced_text = replaced_text + char
        elif(get_emoji_name(char) is not get_emoji_name(previous_char)):
            replaced_text = replaced_text + " " +get_emoji_name(char)[1:-1]+" "
        else:
            #pass
            continue
        
    return replaced_text
        
        
        
#print(replace_emojis_with_text("☺fmgvmn🍜😴😴😴🤯🤯🥴fgfb🤔"))
#print(remove_emoji("HMDA plot sales Agents🤝🏼🏼😜 ;)"))