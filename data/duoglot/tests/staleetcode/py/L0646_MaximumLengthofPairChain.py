
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [[[1, 2], [2, 3], [3, 4]]]
    # output: 2
    # EXPLANATION:  The longest chain is [1,2] -> [3,4].
    ,
    # example 2
    [[[1, 2], [7, 8], [4, 5]]]
    # output: 3
    # EXPLANATION:  The longest chain is [1,2] -> [4,5] -> [7,8].
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
### findLongestChain 
import math
from math import inf
from typing import *
def f_gold(pairs: List[List[int]]) -> int:
    ans, cur = 0, float('-inf')
    for a, b in sorted(pairs, key=lambda x: x[1]):
        if cur < a:
            cur = b
            ans += 1
    return ans
"-----------------"
test()

