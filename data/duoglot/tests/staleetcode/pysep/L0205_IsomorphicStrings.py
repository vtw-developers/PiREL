### isIsomorphic 
from typing import *
def f_gold(s: str, t: str) -> bool:
    d1, d2 = [0] * 256, [0] * 256
    for i, (a, b) in enumerate(zip(s, t)):
        a, b = ord(a), ord(b)
        if d1[a] != d2[b]:
            return False
        d1[a] = d2[b] = i + 1
    return True