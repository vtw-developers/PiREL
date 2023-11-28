### countSegments 
from typing import *
def f_gold(s: str) -> int:
    res = 0
    for i in range(len(s)):
        if s[i] != ' ' and (i == 0 or s[i - 1] == ' '):
            res += 1
    return res