### checkIfExist 
from typing import *
def f_gold(arr: List[int]) -> bool:
    m = {v: i for i, v in enumerate(arr)}
    return any(v << 1 in m and m[v << 1] != i for i, v in enumerate(arr))