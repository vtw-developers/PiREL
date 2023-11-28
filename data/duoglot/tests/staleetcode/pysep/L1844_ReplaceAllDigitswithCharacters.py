### replaceDigits 
from typing import *
def f_gold(s: str) -> str:
    s = list(s)
    for i in range(1, len(s), 2):
        s[i] = chr(ord(s[i - 1]) + int(s[i]))
    return ''.join(s)