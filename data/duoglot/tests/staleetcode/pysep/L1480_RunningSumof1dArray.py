### runningSum 
from itertools import accumulate
from typing import *
def f_gold(nums: List[int]) -> List[int]:
    return list(accumulate(nums))