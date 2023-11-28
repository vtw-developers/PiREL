### removeVowels 
from typing import *
def f_gold(s: str) -> str:
    res = []
    for c in s:
        if c not in {'a', 'e', 'i', 'o', 'u'}:
            res.append(c)
    return ''.join(res)