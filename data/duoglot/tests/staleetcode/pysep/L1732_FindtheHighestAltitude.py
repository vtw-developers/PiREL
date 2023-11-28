### largestAltitude 
from typing import *
def f_gold(gain: List[int]) -> int:
    res = t = 0
    for h in gain:
        t += h
        res = max(res, t)
    return res