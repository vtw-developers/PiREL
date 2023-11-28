### sortArrayByParityII 
from typing import *
def f_gold(nums: List[int]) -> List[int]:
    n, j = len(nums), 1
    for i in range(0, n, 2):
        if (nums[i] & 1) == 1:
            while (nums[j] & 1) == 1:
                j += 2
            nums[i], nums[j] = nums[j], nums[i]
    return nums