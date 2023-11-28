
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [[34, 23, 1, 24, 75, 33, 54, 8], 60]
    # output: 58
    # EXPLANATION: We can use 34 and 24 to sum 58 which is less than 60.
    ,
    # example 2
    [[10, 20, 30], 15]
    # output: -1
    # EXPLANATION: In this case it is not possible to get a pair sum less that 15.
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
### twoSumLessThanK 
from typing import *
def f_gold(nums: List[int], k: int) -> int:
    nums.sort()
    low, high = 0, len(nums) - 1
    res = -1
    while low < high:
        val = nums[low] + nums[high]
        if val < k:
            res = max(res, val)
            low += 1
        else:
            high -= 1
    return res
"-----------------"
test()

