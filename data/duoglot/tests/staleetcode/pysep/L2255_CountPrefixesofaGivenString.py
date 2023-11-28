### countPrefixes 
from typing import *
def f_gold(words: List[str], s: str) -> int:
    return sum(word == s[: len(word)] for word in words)