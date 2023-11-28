### getMaximumConsecutive 
from typing import *
def f_gold(coins: List[int]) -> int:
    res = 1
    for coin in sorted(coins):
        if coin > res:
            break
        res += coin
    return res