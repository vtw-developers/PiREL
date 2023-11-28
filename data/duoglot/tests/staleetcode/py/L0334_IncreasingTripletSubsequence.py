
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [[1, 2, 3, 4, 5]]
    # output: true
    # EXPLANATION:  Any triplet where i < j < k is valid.
    ,
    # example 2
    [[5, 4, 3, 2, 1]]
    # output: false
    # EXPLANATION:  No triplet exists.
    ,
    # example 3
    [[2, 1, 5, 0, 4, 6]]
    # output: true
    # EXPLANATION:  The triplet (3, 4, 5) is valid because nums[3] == 0 < nums[4] == 4 < nums[5] == 6.
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
### increasingTriplet 
import math
from math import inf
from typing import *
def f_gold(nums: List[int]) -> bool:
    mi, mid = float('inf'), float('inf')
    for num in nums:
        if num > mid:
            return True
        if num <= mi:
            mi = num
        else:
            mid = num
    return False
"-----------------"
test()

