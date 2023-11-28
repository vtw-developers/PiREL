### firstMissingPositive 
from typing import *
def f_gold(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    i = 1
    while i in nums:
        i += 1
    return i