### verifyPreorder 
import math
from math import inf
from typing import *
def f_gold(preorder: List[int]) -> bool:
    stk = []
    last = float('-inf')
    for x in preorder:
        if x < last:
            return False
        while stk and stk[-1] < x:
            last = stk.pop()
        stk.append(x)
    return True