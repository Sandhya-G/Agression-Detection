#!/usr/bin/env python
import re
from spellchecker import SpellChecker

#assumes each character doesn't occur more than 2 times at once (really simple logic)
import itertools
def replace_elongated_text(text):
    text = ''.join(''.join(s)[:2] for _, s in itertools.groupby(text))
    return text
#print(replace_elongated_text("aaaaaabbbbbbaaaaccccddc 3333222211 haaaappppyyyyy"))

def words(text): 
    return re.findall('[a-z]+', text.lower()) 

# uses a Levenshtein Distance algorithm to find permutations within an edit distance(dp problem) of 2 from the original word.
def spell_checker(text):
    spell = SpellChecker()
    only_text = " ".join(words(text))
    print(only_text)
    # find those words that may be misspelled
    list_of_words = only_text.strip().split()
    misspelled = spell.unknown(list_of_words)
    #print("mis",misspelled)
    text=text.lower()
    for word in misspelled:
        text = text.replace(word,spell.correction(word))
    return text
#print(spell_checker("3Blue1Vrown"))
#print("10 is a number")
#print(spell_checker("haappyy birtday"))