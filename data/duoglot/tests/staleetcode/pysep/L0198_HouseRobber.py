### rob 
from typing import *
def f_gold(nums: List[int]) -> int:
    a, b = 0, nums[0]
    for num in nums[1:]:
        a, b = b, max(num + a, b)
    return b