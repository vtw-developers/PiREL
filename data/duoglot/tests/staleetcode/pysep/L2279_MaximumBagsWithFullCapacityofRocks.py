### maximumBags 
from typing import *
def f_gold(capacity: List[int], rocks: List[int], additionalRocks: int
) -> int:
    d = [a - b for a, b in zip(capacity, rocks)]
    d.sort()
    ans = 0
    for v in d:
        if v <= additionalRocks:
            ans += 1
            additionalRocks -= v
    return ans