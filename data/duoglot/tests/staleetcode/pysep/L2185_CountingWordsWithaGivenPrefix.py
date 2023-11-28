### prefixCount 
from typing import *
def f_gold(words: List[str], pref: str) -> int:
    return sum(w.startswith(pref) for w in words)