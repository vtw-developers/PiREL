### minEatingSpeed 
from typing import *
def f_gold(piles: List[int], h: int) -> int:
    left, right = 1, int(1e9)
    while left < right:
        mid = (left + right) >> 1
        s = sum((x + mid - 1) // mid for x in piles)
        if s <= h:
            right = mid
        else:
            left = mid + 1
    return left