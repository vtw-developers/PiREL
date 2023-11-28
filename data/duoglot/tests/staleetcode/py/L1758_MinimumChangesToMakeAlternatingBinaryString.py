
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    ["0100"]
    # output: 1
    # EXPLANATION:  If you change the last character to '1', s will be "0101", which is alternating.
    ,
    # example 2
    ["10"]
    # output: 0
    # EXPLANATION:  s is already alternating.
    ,
    # example 3
    ["1111"]
    # output: 2
    # EXPLANATION:  You need two operations to reach "0101" or "1010".
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
### minOperations 
from typing import *
def f_gold(s: str) -> int:
    cnt = 0
    for i, c in enumerate(s):
        cnt += c == '01'[i & 1]
    return min(cnt, len(s) - cnt)
"-----------------"
test()

