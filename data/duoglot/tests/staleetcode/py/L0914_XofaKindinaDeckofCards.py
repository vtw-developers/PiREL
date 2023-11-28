
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [[1, 2, 3, 4, 4, 3, 2, 1]]
    # output: true
    # EXPLANATION: : Possible partition [1,1],[2,2],[3,3],[4,4].
    ,
    # example 2
    [[1, 1, 1, 2, 2, 2, 3, 3]]
    # output: false
    # EXPLANATION: : No possible partition.
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
### hasGroupsSizeX 
from functools import reduce
import math
from math import gcd
from collections import Counter
from typing import *
def f_gold(deck: List[int]) -> bool:
    vals = Counter(deck).values()
    return reduce(gcd, vals) >= 2
"-----------------"
test()

