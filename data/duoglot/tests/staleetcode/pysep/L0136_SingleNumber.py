### singleNumber 
from typing import *
def f_gold(nums: List[int]) -> int:
    res = 0
    for num in nums:
        res ^= num
    return res