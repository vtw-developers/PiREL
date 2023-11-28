
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [2]
    # output: ["1/2"]
    # EXPLANATION:  "1/2" is the only unique fraction with a denominator less-than-or-equal-to 2.
    ,
    # example 2
    [3]
    # output: ["1/2","1/3","2/3"]
    ,
    # example 3
    [4]
    # output: ["1/2","1/3","1/4","2/3","3/4"]
    # EXPLANATION:  "2/4" is not a simplified fraction because it can be simplified to "1/2".
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
### simplifiedFractions 
import math
from math import gcd
from typing import *
def f_gold(n: int) -> List[str]:
    return [
        f'{i}/{j}'
        for i in range(1, n)
        for j in range(i + 1, n + 1)
        if gcd(i, j) == 1
    ]
"-----------------"
test()

