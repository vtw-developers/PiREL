### reversePrefix 
from typing import *
def f_gold(word: str, ch: str) -> str:
    i = word.find(ch)
    return word if i == -1 else word[i::-1] + word[i + 1 :]