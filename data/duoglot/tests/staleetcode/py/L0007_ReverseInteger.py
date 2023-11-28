
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [123]
    # output: 321
    ,
    # example 2
    [-123]
    # output: -321
    ,
    # example 3
    [120]
    # output: 21
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
### reverse 
from typing import *
def f_gold(x: int) -> int:
    y = int(str(abs(x))[::-1])
    res = -y if x < 0 else y
    return 0 if res < -(2**31) or res > 2**31 - 1 else res
"-----------------"
test()

