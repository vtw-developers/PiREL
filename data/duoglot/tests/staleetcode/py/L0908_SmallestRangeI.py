
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [[1], 0]
    # output: 0
    # EXPLANATION:  The score is max(nums) - min(nums) = 1 - 1 = 0.
    ,
    # example 2
    [[0, 10], 2]
    # output: 6
    # EXPLANATION:  Change nums to be [2, 8]. The score is max(nums) - min(nums) = 8 - 2 = 6.
    ,
    # example 3
    [[1, 3, 6], 3]
    # output: 0
    # EXPLANATION:  Change nums to be [4, 4, 4]. The score is max(nums) - min(nums) = 4 - 4 = 0.
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
### smallestRangeI 
from typing import *
def f_gold(nums: List[int], k: int) -> int:
    mx, mi = max(nums), min(nums)
    return max(0, mx - mi - k * 2)
"-----------------"
test()

