### optimalDivision 
from typing import *
def f_gold(nums: List[int]) -> str:
    n = len(nums)
    if n == 1:
        return str(nums[0])
    if n == 2:
        return f'{nums[0]}/{nums[1]}'
    return f'{nums[0]}/({"/".join(map(str, nums[1:]))})'