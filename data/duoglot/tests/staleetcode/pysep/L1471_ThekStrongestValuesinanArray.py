### getStrongest 
from typing import *
def f_gold(arr: List[int], k: int) -> List[int]:
    arr.sort()
    m = arr[(len(arr) - 1) >> 1]
    arr.sort(key=lambda x: (-abs(x - m), -x))
    return arr[:k]