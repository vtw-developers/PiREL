### missingNumber 
from typing import *
def f_gold(nums: List[int]) -> int:
    res = len(nums)
    for i, v in enumerate(nums):
        res ^= i ^ v
    return res