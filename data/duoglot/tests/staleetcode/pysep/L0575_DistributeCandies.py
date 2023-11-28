### distributeCandies 
from typing import *
def f_gold(candyType: List[int]) -> int:
    return min(len(candyType) >> 1, len(set(candyType)))