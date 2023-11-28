### sortEvenOdd 
from typing import *
def f_gold(nums: List[int]) -> List[int]:
    a = sorted(nums[::2])
    b = sorted(nums[1::2], reverse=True)
    nums[::2] = a
    nums[1::2] = b
    return nums