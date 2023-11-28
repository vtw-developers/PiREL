### maxDepth 
from typing import *
def f_gold(s: str) -> int:
    n = ans = 0
    for c in s:
        if c == '(':
            n += 1
            ans = max(ans, n)
        elif c == ')':
            n -= 1
    return ans