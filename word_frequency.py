#!/usr/bin/env python3

# Word frequency exercise
# TODO: (Read detailed instructions in the Readme file)

import re

# This is a function that checks if a text qualifies as a sentence. 
# You do not need to modify this!
def is_sentence(text):
    # Check if the text is not empty and is a string
    if not isinstance(text, str) or not text.strip():
        return False

    # Check for starting with a capital letter
    if not text[0].isupper():
        return False

    # Check for ending punctuation
    if not re.search(r'[.!?]$', text):
        return False

    # Check if it contains at least one word (non-whitespace characters)
    if not re.search(r'\w+', text):
        return False

    return True


# -----------------------------
# You do NOT modify the code above.
# Add your functions below.
# -----------------------------

def get_sentence():
    """Prompt the user for a valid sentence using the is_sentence() function."""
    while True:
        sentence = input("Enter a sentence: ").strip()
        if is_sentence(sentence):
            return sentence
        else:
            print("Invalid sentence. It must start with a capital letter and end with punctuation (!?.)")


def calculate_frequencies(sentence):
    """Return two lists: one for words, one for their frequencies."""
    words = []
    frequencies = []
    for word in sentence[:-1].lower().split():
        word = word.strip(",;:-_\"'()[]{}")
        if word in words:
            index = words.index(word)
            frequencies[index] += 1
        else:
            words.append(word)
            frequencies.append(1)
    return words, frequencies


def print_frequencies(words, frequencies):
    ""
