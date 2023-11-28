### removeDuplicates 
from typing import *
def f_gold(nums: List[int]) -> int:
    i = 0
    for num in nums:
        if i < 1 or num != nums[i - 1]:
            nums[i] = num
            i += 1
    return i