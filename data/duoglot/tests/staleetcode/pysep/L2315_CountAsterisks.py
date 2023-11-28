### countAsterisks 
from typing import *
def f_gold(s: str) -> int:
    ans = t = 0
    for c in s:
        if c == '|':
            t ^= 1
        elif c == '*':
            if t == 0:
                ans += 1
    return ans