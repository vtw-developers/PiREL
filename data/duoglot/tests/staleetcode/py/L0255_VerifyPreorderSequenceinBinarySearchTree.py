
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [[5, 2, 1, 3, 6]]
    # output: true
    ,
    # example 2
    [[5, 2, 6, 1, 3]]
    # output: false
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
### verifyPreorder 
import math
from math import inf
from typing import *
def f_gold(preorder: List[int]) -> bool:
    stk = []
    last = float('-inf')
    for x in preorder:
        if x < last:
            return False
        while stk and stk[-1] < x:
            last = stk.pop()
        stk.append(x)
    return True
"-----------------"
test()

