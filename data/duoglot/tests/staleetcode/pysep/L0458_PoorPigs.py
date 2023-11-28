### poorPigs 
from typing import *
def f_gold(buckets: int, minutesToDie: int, minutesToTest: int) -> int:
    base = minutesToTest // minutesToDie + 1
    res, p = 0, 1
    while p < buckets:
        p *= base
        res += 1
    return res