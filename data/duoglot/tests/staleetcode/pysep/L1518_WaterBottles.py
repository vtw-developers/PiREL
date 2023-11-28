### numWaterBottles 
from typing import *
def f_gold(numBottles: int, numExchange: int) -> int:
    ans = numBottles
    while numBottles >= numExchange:
        numBottles -= numExchange - 1
        ans += 1
    return ans