### maximumXOR 
from typing import *
def f_gold(nums: List[int]) -> int:
    ans = 0
    for v in nums:
        ans |= v
    return ans