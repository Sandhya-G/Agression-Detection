#!/usr/bin/env python

from spellchecker import SpellChecker

#assumes each character doesn't occur more than 2 times at once (really simple logic)
import itertools
def replace_elongated_text(text):
    text = ''.join(''.join(s)[:2] for _, s in itertools.groupby(text))
    return text
print(replace_elongated_text("aaaaaabbbbbbaaaaccccddc haaaappppyyyyy"))

## uses a Levenshtein Distance algorithm to find permutations within an edit distance(dp problem) of 2 from the original word.

def spell_checker(text):
    spell = SpellChecker()
    # find those words that may be misspelled
    list_of_words = text.split()
    misspelled = spell.unknown(list_of_words)
    new_text = ''
    for word in list_of_words:
        new_text = new_text + " " +spell.correction(word) if word in misspelled else word
    return new_text
print(spell_checker("haappyy birtday"))