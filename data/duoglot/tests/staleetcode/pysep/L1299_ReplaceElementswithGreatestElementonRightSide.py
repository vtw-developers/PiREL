### replaceElements 
from typing import *
def f_gold(arr: List[int]) -> List[int]:
    m = -1
    for i in range(len(arr) - 1, -1, -1):
        t = arr[i]
        arr[i] = m
        m = max(m, t)
    return arr