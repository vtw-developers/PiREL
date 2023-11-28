
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [3, 3, [[2, 2], [3, 3]]]
    # output: 4
    # EXPLANATION:  The maximum integer in M is 2, and there are four of it in M. So return 4.
    ,
    # example 2
    [3, 3, [[2, 2], [3, 3], [3, 3], [3, 3], [2, 2], [3, 3], [3, 3], [3, 3], [2, 2], [3, 3], [3, 3], [3, 3]]]
    # output: 4
    ,
    # example 3
    [3, 3, []]
    # output: 9
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
### maxCount 
from typing import *
def f_gold(m: int, n: int, ops: List[List[int]]) -> int:
    for a, b in ops:
        m = min(m, a)
        n = min(n, b)
    return m * n
"-----------------"
test()

