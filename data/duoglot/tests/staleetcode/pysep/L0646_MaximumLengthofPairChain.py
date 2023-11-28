### findLongestChain 
import math
from math import inf
from typing import *
def f_gold(pairs: List[List[int]]) -> int:
    ans, cur = 0, float('-inf')
    for a, b in sorted(pairs, key=lambda x: x[1]):
        if cur < a:
            cur = b
            ans += 1
    return ans