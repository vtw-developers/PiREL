### targetIndices 
from typing import *
def f_gold(nums: List[int], target: int) -> List[int]:
    nums.sort()
    return [i for i, num in enumerate(nums) if num == target]