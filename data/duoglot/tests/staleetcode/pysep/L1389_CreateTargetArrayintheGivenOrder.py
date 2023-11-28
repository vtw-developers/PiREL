### createTargetArray 
from typing import *
def f_gold(nums: List[int], index: List[int]) -> List[int]:
    target = []
    for i in range(len(nums)):
        target.insert(index[i], nums[i])
    return target