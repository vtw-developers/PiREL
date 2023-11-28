### truncateSentence 
from typing import *
def f_gold(s: str, k: int) -> str:
    for i, c in enumerate(s):
        if c == ' ':
            k -= 1
        if k == 0:
            return s[:i]
    return s