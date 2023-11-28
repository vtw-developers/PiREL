### maxCount 
from typing import *
def f_gold(m: int, n: int, ops: List[List[int]]) -> int:
    for a, b in ops:
        m = min(m, a)
        n = min(n, b)
    return m * n