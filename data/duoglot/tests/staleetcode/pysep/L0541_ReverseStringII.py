### reverseStr 
from typing import *
def f_gold(s: str, k: int) -> str:
    t = list(s)
    for i in range(0, len(t), k << 1):
        t[i : i + k] = reversed(t[i : i + k])
    return ''.join(t)