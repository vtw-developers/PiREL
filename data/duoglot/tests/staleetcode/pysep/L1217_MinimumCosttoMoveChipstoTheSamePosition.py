### minCostToMoveChips 
from typing import *
def f_gold(position: List[int]) -> int:
    a = sum(p % 2 for p in position)
    b = len(position) - a
    return min(a, b)