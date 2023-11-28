
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    ["RLRRLLRLRL"]
    # output: 4
    # EXPLANATION:  s can be split into "RL", "RRLL", "RL", "RL", each substring contains same number of 'L' and 'R'.
    ,
    # example 2
    ["RLLLLRRRLR"]
    # output: 3
    # EXPLANATION:  s can be split into "RL", "LLLRRR", "LR", each substring contains same number of 'L' and 'R'.
    ,
    # example 3
    ["LLLLRRRR"]
    # output: 1
    # EXPLANATION:  s can be split into "LLLLRRRR".
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
### balancedStringSplit 
from typing import *
def f_gold(s: str) -> int:
    n = res = 0
    for c in s:
        if c == 'L':
            n += 1
        else:
            n -= 1
        if n == 0:
            res += 1
    return res
"-----------------"
test()

