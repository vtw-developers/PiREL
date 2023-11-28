### maxProfit 
from typing import *
def f_gold(prices: List[int]) -> int:
    res, mi = 0, prices[0]
    for price in prices[1:]:
        res = max(res, price - mi)
        mi = min(mi, price)
    return res