### heightChecker 
from typing import *
def f_gold(heights: List[int]) -> int:
    expected = sorted(heights)
    return sum(a != b for a, b in zip(heights, expected))