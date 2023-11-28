
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [[1, 1, 0, 1, 1, 1]]
    # output: 3
    # EXPLANATION:  The first two digits or the last three digits are consecutive 1s. The maximum number of consecutive 1s is 3.
    ,
    # example 2
    [[1, 0, 1, 1, 0, 1]]
    # output: 2
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
### findMaxConsecutiveOnes 
from typing import *
def f_gold(nums: List[int]) -> int:
    res = t = 0
    for num in nums:
        if num == 1:
            t += 1
        else:
            res = max(res, t)
            t = 0
    return max(res, t)
"-----------------"
test()

