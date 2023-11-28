### isPrefixOfWord 
from typing import *
def f_gold(sentence: str, searchWord: str) -> int:
    words = sentence.split(' ')
    i, n = 0, len(words)
    while i < n:
        word = words[i]
        if word[: len(searchWord)] == searchWord:
            return i + 1
        i += 1
    return -1