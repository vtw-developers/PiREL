### removeAnagrams 
from typing import *
def f_gold(words: List[str]) -> List[str]:
    return [
        w
        for i, w in enumerate(words)
        if i == 0 or sorted(w) != sorted(words[i - 1])
    ]