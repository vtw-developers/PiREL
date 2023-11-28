
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [5, 7]
    # output: 4
    ,
    # example 2
    [0, 0]
    # output: 0
    ,
    # example 3
    [1, 2147483647]
    # output: 0
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
### rangeBitwiseAnd 
from typing import *
def f_gold(left: int, right: int) -> int:
    while left < right:
        right &= right - 1
    return right
"-----------------"
test()

