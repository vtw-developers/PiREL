
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [[1, 2, 10, 5, 7]]
    # output: true
    # EXPLANATION:  By removing 10 at index 2 from nums, it becomes [1,2,5,7]. [1,2,5,7] is strictly increasing, so return true.
    ,
    # example 2
    [[2, 3, 1, 2]]
    # output: false
    # EXPLANATION:  [3,1,2] is the result of removing the element at index 0. [2,1,2] is the result of removing the element at index 1. [2,3,2] is the result of removing the element at index 2. [2,3,1] is the result of removing the element at index 3. No resulting array is strictly increasing, so return false.
    ,
    # example 3
    [[1, 1, 1]]
    # output: false
    # EXPLANATION:  The result of removing any element is [1,1]. [1,1] is not strictly increasing, so return false.
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
### canBeIncreasing 
import math
from math import inf
from typing import *
def f_gold(nums: List[int]) -> bool:
    def check(nums, i):
        prev = float('-inf')
        for j, num in enumerate(nums):
            if i == j:
                continue
            if prev >= nums[j]:
                return False
            prev = nums[j]
        return True
    i, n = 1, len(nums)
    while i < n and nums[i - 1] < nums[i]:
        i += 1
    return check(nums, i - 1) or check(nums, i)
"-----------------"
test()

