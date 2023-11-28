### arrayPairSum 
from typing import *
def f_gold(nums: List[int]) -> int:
    return sum(sorted(nums)[::2])