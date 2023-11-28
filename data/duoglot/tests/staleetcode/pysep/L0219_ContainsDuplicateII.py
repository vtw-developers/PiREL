### containsNearbyDuplicate 
from typing import *
def f_gold(nums: List[int], k: int) -> bool:
    mp = {}
    for i, v in enumerate(nums):
        if v in mp and i - mp[v] <= k:
            return True
        mp[v] = i
    return False