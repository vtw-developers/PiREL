
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [[2, 3, 1, 1, 4]]
    # output: true
    # EXPLANATION:  Jump 1 step from index 0 to 1, then 3 steps to the last index.
    ,
    # example 2
    [[3, 2, 1, 0, 4]]
    # output: false
    # EXPLANATION:  You will always arrive at index 3 no matter what. Its maximum jump length is 0, which makes it impossible to reach the last index.
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
### canJump 
from typing import *
def f_gold(nums: List[int]) -> bool:
    mx = 0
    for i, num in enumerate(nums):
        if i > mx:
            return False
        mx = max(mx, i + num)
    return True
"-----------------"
test()

