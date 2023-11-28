### longestPrefix 
from typing import *
def f_gold(s: str) -> str:
    for i in range(1, len(s)):
        if s[:-i] == s[i:]:
            return s[i:]
    return ''