### findTheDistanceValue 
from typing import *
def f_gold(arr1: List[int], arr2: List[int], d: int) -> int:
    return sum(all(abs(a - b) > d for b in arr2) for a in arr1)