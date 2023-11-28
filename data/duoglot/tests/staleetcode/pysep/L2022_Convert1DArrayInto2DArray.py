### construct2DArray 
from typing import *
def f_gold(original: List[int], m: int, n: int) -> List[List[int]]:
    if m * n != len(original):
        return []
    return [original[i : i + n] for i in range(0, m * n, n)]