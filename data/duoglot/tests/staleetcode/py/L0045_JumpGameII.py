
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [[2, 3, 1, 1, 4]]
    # output: 2
    # EXPLANATION:  The minimum number of jumps to reach the last index is 2. Jump 1 step from index 0 to 1, then 3 steps to the last index.
    ,
    # example 2
    [[2, 3, 0, 1, 4]]
    # output: 2
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
### jump 
from typing import *
def f_gold(nums: List[int]) -> int:
    end = mx = steps = 0
    for i, num in enumerate(nums[:-1]):
        mx = max(mx, i + num)
        if i == end:
            end = mx
            steps += 1
    return steps
"-----------------"
test()

