### findLucky 
from collections import Counter
from typing import *
def f_gold(arr: List[int]) -> int:
    counter = Counter(arr)
    ans = -1
    for num, n in counter.items():
        if num == n and ans < num:
            ans = num
    return ans