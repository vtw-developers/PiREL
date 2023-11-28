### sortSentence 
from typing import *
def f_gold(s: str) -> str:
    words = s.split(' ')
    arr = [None] * len(words)
    for word in words:
        idx = int(word[-1]) - 1
        arr[idx] = word[:-1]
    return ' '.join(arr)