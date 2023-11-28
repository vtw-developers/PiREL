### checkIfPangram 
from typing import *
def f_gold(sentence: str) -> bool:
    res = 0
    for c in sentence:
        res |= 1 << (ord(c) - ord('a'))
        if res == 0x3FFFFFF:
            return True
    return False