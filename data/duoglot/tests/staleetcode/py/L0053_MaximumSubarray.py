
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [[-2, 1, -3, 4, -1, 2, 1, -5, 4]]
    # output: 6
    # EXPLANATION:  [4,-1,2,1] has the largest sum = 6.
    ,
    # example 2
    [[1]]
    # output: 1
    ,
    # example 3
    [[5, 4, -1, 7, 8]]
    # output: 23
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
### maxSubArray 
from typing import *
def f_gold(nums: List[int]) -> int:
    res = f = nums[0]
    for num in nums[1:]:
        f = num + max(f, 0)
        res = max(res, f)
    return res
"-----------------"
test()

