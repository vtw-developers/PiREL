### divideArray 
from collections import Counter
from typing import *
def f_gold(nums: List[int]) -> bool:
    cnt = Counter(nums)
    return all(v % 2 == 0 for v in cnt.values())