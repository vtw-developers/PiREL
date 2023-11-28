### carPooling 
from itertools import accumulate
from typing import *
def f_gold(trips: List[List[int]], capacity: int) -> bool:
    delta = [0] * 1001
    for num, start, end in trips:
        delta[start] += num
        delta[end] -= num
    return all(s <= capacity for s in accumulate(delta))