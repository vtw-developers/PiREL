### minSwaps 
from typing import *
def f_gold(s: str) -> int:
    ans = 0
    for c in s:
        if c == '[':
            ans += 1
        elif ans:
            ans -= 1
    return (ans + 1) >> 1