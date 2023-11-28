### removeDuplicates 
from typing import *
def f_gold(S: str) -> str:
    res = []
    for s in S:
        if not res or res[-1] != s:
            res.append(s)
        else:
            res.pop()
    return ''.join(res)