### minMoves 
from typing import *
def f_gold(nums: List[int]) -> int:
    return sum(nums) - min(nums) * len(nums)