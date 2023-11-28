
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [4]
    # output: 2
    ,
    # example 2
    [8]
    # output: 2
    # EXPLANATION:  The square root of 8 is 2.82842..., and since the decimal part is truncated, 2 is returned.
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
### mySqrt 
from typing import *
def f_gold(x: int) -> int:
    left, right = 0, x
    while left < right:
        mid = (left + right + 1) >> 1
        # mid*mid <= x
        if mid <= x // mid:
            left = mid
        else:
            right = mid - 1
    return left
"-----------------"
test()

