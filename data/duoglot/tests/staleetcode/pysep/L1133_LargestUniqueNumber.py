### largestUniqueNumber 
from collections import Counter
from typing import *
def f_gold(A: List[int]) -> int:
    counter = Counter(A)
    for i in range(1000, -1, -1):
        if counter[i] == 1:
            return i
    return -1