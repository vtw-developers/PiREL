### addRungs 
from typing import *
def f_gold(rungs: List[int], dist: int) -> int:
    prev = res = 0
    for rung in rungs:
        res += (rung - prev - 1) // dist
        prev = rung
    return res