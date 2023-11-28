
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [16]
    # output: true
    ,
    # example 2
    [14]
    # output: false
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
### isPerfectSquare 
from typing import *
def f_gold(num: int) -> bool:
    left, right = 1, num
    while left < right:
        mid = (left + right) >> 1
        if mid * mid >= num:
            right = mid
        else:
            left = mid + 1
    return left * left == num
"-----------------"
test()

