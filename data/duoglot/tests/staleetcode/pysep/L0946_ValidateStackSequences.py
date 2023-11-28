### validateStackSequences 
from typing import *
def f_gold(pushed: List[int], popped: List[int]) -> bool:
    stk, j, n = [], 0, len(popped)
    for x in pushed:
        stk.append(x)
        while stk and j < n and stk[-1] == popped[j]:
            stk.pop()
            j += 1
    return j == n