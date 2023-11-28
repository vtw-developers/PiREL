
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [5]
    # output: true
    # EXPLANATION:  1 * 1 + 2 * 2 = 5
    ,
    # example 2
    [3]
    # output: false
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
### judgeSquareSum 
import math
from math import sqrt
from typing import *
def f_gold(c: int) -> bool:
    a, b = 0, int(sqrt(c))
    while a <= b:
        s = a**2 + b**2
        if s == c:
            return True
        if s < c:
            a += 1
        else:
            b -= 1
    return False
"-----------------"
test()

