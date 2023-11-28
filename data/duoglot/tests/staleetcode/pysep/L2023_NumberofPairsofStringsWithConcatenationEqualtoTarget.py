### numOfPairs 
from typing import *
def f_gold(nums: List[str], target: str) -> int:
    n = len(nums)
    return sum(
        i != j and nums[i] + nums[j] == target for i in range(n) for j in range(n)
    )