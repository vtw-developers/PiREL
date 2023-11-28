### shuffle 
from typing import *
def f_gold(nums: List[int], n: int) -> List[int]:
    ans = []
    for i in range(n):
        ans.append(nums[i])
        ans.append(nums[i + n])
    return ans