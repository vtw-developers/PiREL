### isPrefixString 
from typing import *
def f_gold(s: str, words: List[str]) -> bool:
    t = 0
    for i, w in enumerate(words):
        t += len(w)
        if len(s) == t:
            return ''.join(words[: i + 1]) == s
    return False