### maxChunksToSorted 
from typing import *
def f_gold(arr: List[int]) -> int:
    stk = []
    for v in arr:
        if not stk or v >= stk[-1]:
            stk.append(v)
        else:
            mx = stk.pop()
            while stk and stk[-1] > v:
                stk.pop()
            stk.append(mx)
    return len(stk)