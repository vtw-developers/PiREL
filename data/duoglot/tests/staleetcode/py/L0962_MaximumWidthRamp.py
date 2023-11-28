
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [[6, 0, 8, 2, 1, 5]]
    # output: 4
    # EXPLANATION:  The maximum width ramp is achieved at (i, j) = (1, 5): nums[1] = 0 and nums[5] = 5.
    ,
    # example 2
    [[9, 8, 1, 0, 1, 9, 4, 0, 4, 1]]
    # output: 7
    # EXPLANATION:  The maximum width ramp is achieved at (i, j) = (2, 9): nums[2] = 1 and nums[9] = 1.
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
### maxWidthRamp 
from typing import *
def f_gold(nums: List[int]) -> int:
    stk = []
    for i, v in enumerate(nums):
        if not stk or nums[stk[-1]] > v:
            stk.append(i)
    ans = 0
    for i in range(len(nums) - 1, -1, -1):
        while stk and nums[stk[-1]] <= nums[i]:
            ans = max(ans, i - stk.pop())
        if not stk:
            break
    return ans
"-----------------"
test()

