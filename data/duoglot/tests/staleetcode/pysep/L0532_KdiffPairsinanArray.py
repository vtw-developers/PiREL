### findPairs 
from typing import *
def f_gold(nums: List[int], k: int) -> int:
    vis, ans = set(), set()
    for v in nums:
        if v - k in vis:
            ans.add(v - k)
        if v + k in vis:
            ans.add(v)
        vis.add(v)
    return len(ans)