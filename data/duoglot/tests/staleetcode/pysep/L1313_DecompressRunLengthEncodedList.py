### decompressRLElist 
from typing import *
def f_gold(nums: List[int]) -> List[int]:
    res = []
    for i in range(1, len(nums), 2):
        res.extend([nums[i]] * nums[i - 1])
    return res