### canBeEqual 
from typing import *
def f_gold(target: List[int], arr: List[int]) -> bool:
    return sorted(target) == sorted(arr)