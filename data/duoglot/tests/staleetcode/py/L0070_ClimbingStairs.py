
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [2]
    # output: 2
    # EXPLANATION:  There are two ways to climb to the top. 1. 1 step + 1 step 2. 2 steps
    ,
    # example 2
    [3]
    # output: 3
    # EXPLANATION:  There are three ways to climb to the top. 1. 1 step + 1 step + 1 step 2. 1 step + 2 steps 3. 2 steps + 1 step
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
### climbStairs 
from typing import *
def f_gold(n: int) -> int:
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return b
"-----------------"
test()

