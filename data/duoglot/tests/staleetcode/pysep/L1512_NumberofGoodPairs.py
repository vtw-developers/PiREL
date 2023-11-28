### numIdenticalPairs 
from collections import Counter
from typing import *
def f_gold(nums: List[int]) -> int:
    counter = Counter(nums)
    return sum([x * (x - 1) for x in counter.values()]) >> 1