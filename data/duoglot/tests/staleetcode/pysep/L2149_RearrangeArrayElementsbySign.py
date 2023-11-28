### rearrangeArray 
from typing import *
def f_gold(nums: List[int]) -> List[int]:
    ans = [0] * len(nums)
    i, j = 0, 1
    for num in nums:
        if num > 0:
            ans[i] = num
            i += 2
        else:
            ans[j] = num
            j += 2
    return ans