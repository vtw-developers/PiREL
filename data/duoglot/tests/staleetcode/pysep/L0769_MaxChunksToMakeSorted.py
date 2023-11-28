### maxChunksToSorted 
from typing import *
def f_gold(arr: List[int]) -> int:
    mx = ans = 0
    for i, v in enumerate(arr):
        mx = max(mx, v)
        if i == mx:
            ans += 1
    return ans