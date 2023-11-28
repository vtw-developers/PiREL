
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [[2, 3, -1, 8, 4]]
    # output: 3
    # EXPLANATION:  The sum of the numbers before index 3 is: 2 + 3 + -1 = 4 The sum of the numbers after index 3 is: 4 = 4
    ,
    # example 2
    [[1, -1, 4]]
    # output: 2
    # EXPLANATION:  The sum of the numbers before index 2 is: 1 + -1 = 0 The sum of the numbers after index 2 is: 0
    ,
    # example 3
    [[2, 5]]
    # output: -1
    # EXPLANATION:  There is no valid middleIndex.
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
### findMiddleIndex 
from typing import *
def f_gold(nums: List[int]) -> int:
    s = sum(nums)
    total = 0
    for i, num in enumerate(nums):
        total += num
        if total - num == s - total:
            return i
    return -1
"-----------------"
test()

