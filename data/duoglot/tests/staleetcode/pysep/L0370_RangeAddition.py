### getModifiedArray 
from itertools import accumulate
from typing import *
def f_gold(length: int, updates: List[List[int]]) -> List[int]:
    delta = [0] * length
    for start, end, inc in updates:
        delta[start] += inc
        if end + 1 < length:
            delta[end + 1] -= inc
    return list(accumulate(delta))