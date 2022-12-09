import random

def verify(words):
    word = random.choice(words)
    while '-' in word and ' ' in word:
        word = random.choice(words)
    return word.upper()