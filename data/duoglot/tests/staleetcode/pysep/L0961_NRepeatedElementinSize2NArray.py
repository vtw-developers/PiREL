### repeatedNTimes 
from typing import *
def f_gold(nums: List[int]) -> int:
    s = set()
    for num in nums:
        if num in s:
            return num
        s.add(num)