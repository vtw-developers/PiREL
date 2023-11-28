### kidsWithCandies 
from typing import *
def f_gold(candies: List[int], extraCandies: int) -> List[bool]:
    mx = max(candies)
    return [candy + extraCandies >= mx for candy in candies]