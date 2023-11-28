
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [2.0, 10]
    # output: 1024.00000
    ,
    # example 2
    [2.1, 3]
    # output: 9.26100
    ,
    # example 3
    [2.0, -2]
    # output: 0.25000
    # EXPLANATION:  2<sup>-2</sup> = 1/2<sup>2</sup> = 1/4 = 0.25
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
### myPow 
from typing import *
def f_gold(x: float, n: int) -> float:
    if n == 0:
        return 1
    if n < 0:
        return 1 / f_gold(x, -n)
    y = f_gold(x, n >> 1)
    return y * y if (n & 1) == 0 else y * y * x
"-----------------"
test()

