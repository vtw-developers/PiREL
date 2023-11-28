### containsDuplicate 
from typing import *
def f_gold(nums: List[int]) -> bool:
    return len(set(nums)) < len(nums)