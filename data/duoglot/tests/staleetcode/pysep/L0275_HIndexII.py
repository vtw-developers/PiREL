### hIndex 
from typing import *
def f_gold(citations: List[int]) -> int:
    n = len(citations)
    left, right = 0, n
    while left < right:
        mid = (left + right + 1) >> 1
        if citations[n - mid] >= mid:
            left = mid
        else:
            right = mid - 1
    return left