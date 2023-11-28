### minTimeToType 
from typing import *
def f_gold(word: str) -> int:
    ans = prev = 0
    for c in word:
        curr = ord(c) - ord('a')
        t = abs(prev - curr)
        t = min(t, 26 - t)
        ans += t + 1
        prev = curr
    return ans