### minAddToMakeValid 
from typing import *
def f_gold(s: str) -> int:
    stk = []
    for c in s:
        if c == '(':
            stk.append(c)
        else:
            if stk and stk[-1] == '(':
                stk.pop()
            else:
                stk.append(c)
    return len(stk)