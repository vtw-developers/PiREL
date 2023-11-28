### sumOfUnique 
from collections import Counter
from typing import *
def f_gold(nums: List[int]) -> int:
    counter = Counter(nums)
    return sum(num for num, cnt in counter.items() if cnt == 1)