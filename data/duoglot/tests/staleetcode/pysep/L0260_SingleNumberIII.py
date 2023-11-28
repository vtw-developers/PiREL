### singleNumber 
from typing import *
def f_gold(nums: List[int]) -> List[int]:
    eor = 0
    for x in nums:
        eor ^= x
    lowbit = eor & (-eor)
    ans = [0, 0]
    for x in nums:
        if (x & lowbit) == 0:
            ans[0] ^= x
    ans[1] = eor ^ ans[0]
    return ans