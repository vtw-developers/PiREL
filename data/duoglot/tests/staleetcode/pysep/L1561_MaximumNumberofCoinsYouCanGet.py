### maxCoins 
from typing import *
def f_gold(piles: List[int]) -> int:
    piles.sort()
    return sum(piles[-2 : len(piles) // 3 - 1 : -2])