
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [[1, 2, 3]]
    # output: 6
    ,
    # example 2
    [[1, 2, 3, 4]]
    # output: 24
    ,
    # example 3
    [[-1, -2, -3]]
    # output: -6
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
### maximumProduct 
from typing import *
def f_gold(nums: List[int]) -> int:
    n = len(nums)
    nums.sort()
    return max(
        nums[0] * nums[1] * nums[n - 1], nums[n - 1] * nums[n - 2] * nums[n - 3]
    )
"-----------------"
test()

