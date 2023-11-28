
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [5]
    # output: 2
    # EXPLANATION: : The square triples are (3,4,5) and (4,3,5).
    ,
    # example 2
    [10]
    # output: 4
    # EXPLANATION: : The square triples are (3,4,5), (4,3,5), (6,8,10), and (8,6,10).
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
### countTriples 
import math
from math import sqrt
from typing import *
def f_gold(n: int) -> int:
    res = 0
    for a in range(1, n + 1):
        for b in range(1, n + 1):
            t = a**2 + b**2
            c = int(sqrt(t))
            if c <= n and c**2 == t:
                res += 1
    return res
"-----------------"
test()

