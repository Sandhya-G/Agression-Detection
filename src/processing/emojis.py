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

#def replace_emoji_for_glove(tweet,embedding):
    #emoji_only = extract_emoji(tweet)
    #for e in emoji_only:
        #if e not in embedding:
            #tweet = tweet.replace(e,get_emoji_name(e)[1:-1])
    #return tweet
def remove_duplicates(text):
    assert isinstance(text,str) and len(text)>0,"size must be greater than 0" 
    new_text = ''
    text = text.strip()
    for word in text.split():
        
        new_text = new_text+" " +word[0]
        #print("new_text",new_text,"\n")
        for i in range(1,len(word)):
            if is_emoji(word[i]) and is_emoji(word[i-1]) and (get_emoji_name(word[i]) == get_emoji_name(word[i-1])):
                continue
            else:
                new_text = new_text + word[i]
    return new_text.strip()



def replace_emojis_with_text(text):
    text = remove_duplicates(text)
    for word in text.split():
        for i in range(0,len(word)):
            if is_emoji(word[i]):
                text = text.replace(word[i]," " +get_emoji_name(word[i])[1:-1]+" ")
    return text.strip()

    
        
        
        
print(replace_emojis_with_text("☺fmgvmn🍜😴😴😴🤯🤯🥴fgfb🤔"))
#print(remove_emoji("HMDA plot sales Agents🤝🏼🏼😜 ;)"))