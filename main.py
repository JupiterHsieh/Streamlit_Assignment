import time
import streamlit as st
import numpy as np
import pandas as pd
import re
from collections import Counter



def words(text): return re.findall(r'\w+', text.lower())

WORDS = Counter(words(open('big.txt').read()))

def P(word, N=sum(WORDS.values())): 
    "Probability of `word`."
    return WORDS[word] / N 

def correct(word):
    "Find the best spelling correction for this word."
    return max(candidates, key=COUNTS.get)

def correction(word): 
    "Most probable spelling correction for word."
    return max(candidates(word), key=P)


def candidates(word): 
    "Generate possible spelling corrections for word."
    return (known([word]) or known(edits0(word)) 
            or known(edits1(word)) or known(edits2(word)) or [word])

def known(words): 
    "The subset of `words` that appear in the dictionary of WORDS."
    return set(w for w in words if w in WORDS)

def edits0(word):
    letters    = 'abcdefghijklmnopqrstuvwxyz'
    splits     = [(word[:i], word[i:])    for i in range(len(word) + 1)]   
    replaces = []
    lettersa    = 'f'
    replaces.extend([L + "gh" + R[1:]           for L, R in splits if (len(R)==1 and R=="f")])
    lettersb    = 'cs'
    replaces.extend([L + c + R[1:]           for L, R in splits if R if R[0] in lettersb for c in lettersb])
    lettersc = 'aeiou'
    replaces.extend([L + c + R[1:]           for L, R in splits if R if R[0] in lettersc for c in lettersc])
    lettersd = 'mn'
    replaces.extend([L + c + R[1:]           for L, R in splits if R if R[0] in lettersd for c in lettersd]) 
    replaces.extend([L + R[0] + R[0] + R[1:] for L, R in splits if R])
    inserts    = [L + c + R               for L, R in splits for c in letters]
    return set(replaces+inserts)

def edits1(word):
    "All edits that are one edit away from `word`."
    letters    = 'abcdefghijklmnopqrstuvwxyz'
    splits     = [(word[:i], word[i:])    for i in range(len(word) + 1)]
    deletes    = [L + R[1:]               for L, R in splits if R]
    transposes = [L + R[1] + R[0] + R[2:] for L, R in splits if len(R)>1]
    replaces   = [L + c + R[1:]           for L, R in splits if R for c in letters]
    inserts    = [L + c + R               for L, R in splits for c in letters]
    return set(deletes + transposes + replaces + inserts)

def edits2(word): 
    "All edits that are two edits away from `word`."
    return (e2 for e1 in edits1(word) for e2 in edits1(e1))

def known(words): return set(w for w in words if w in WORDS)

def words(text): return re.findall(r'\w+', text.lower())


WORDS = Counter(words(open('big.txt').read()))
def P(word, N=sum(WORDS.values())): return WORDS[word] / N



show = st.sidebar.checkbox(
'Show original word'
)

# Using "with" notation



st.title("Spellchecker Demo")
option = st.selectbox(
    'Choose a word or...',
    ('apple', 'lamon', 'hapy','speling','language','greay'))


word_check = st.text_input('type your own',value=option)

if show:
    st.markdown('Original word: {}'.format(word_check))

if correction(word_check) == word_check:
    st.success("{} is the correct spelling!".format(word_check))
else:
    st.error("Correction: {}".format(correction(word_check)))
    










