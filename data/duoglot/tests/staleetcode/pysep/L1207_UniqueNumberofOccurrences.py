### uniqueOccurrences 
from collections import Counter
from typing import *
def f_gold(arr: List[int]) -> bool:
    counter = Counter(arr)
    s = set()
    for num in counter.values():
        if num in s:
            return False
        s.add(num)
    return True