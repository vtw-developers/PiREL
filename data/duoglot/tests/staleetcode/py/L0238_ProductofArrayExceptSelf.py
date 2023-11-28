
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [[1, 2, 3, 4]]
    # output: [24,12,8,6]
    ,
    # example 2
    [[-1, 1, 0, -3, 3]]
    # output: [0,0,9,0,0]
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
### productExceptSelf 
from typing import *
def f_gold(nums: List[int]) -> List[int]:
    n = len(nums)
    ans = [1] * n
    left = right = 1
    for i in range(n):
        ans[i] = left
        left *= nums[i]
    for i in range(n - 1, -1, -1):
        ans[i] *= right
        right *= nums[i]
    return ans
"-----------------"
test()

