### calPoints 
from typing import *
def f_gold(ops: List[str]) -> int:
    stk = []
    for op in ops:
        if op == '+':
            stk.append(stk[-1] + stk[-2])
        elif op == 'D':
            stk.append(stk[-1] << 1)
        elif op == 'C':
            stk.pop()
        else:
            stk.append(int(op))
    return sum(stk)