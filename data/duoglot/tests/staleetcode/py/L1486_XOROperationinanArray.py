
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [5, 0]
    # output: 8
    # EXPLANATION:  Array nums is equal to [0, 2, 4, 6, 8] where (0 ^ 2 ^ 4 ^ 6 ^ 8) = 8. Where "^" corresponds to bitwise XOR operator.
    ,
    # example 2
    [4, 3]
    # output: 8
    # EXPLANATION:  Array nums is equal to [3, 5, 7, 9] where (3 ^ 5 ^ 7 ^ 9) = 8.
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
### xorOperation 
from typing import *
def f_gold(n: int, start: int) -> int:
    res = 0
    for i in range(n):
        res ^= start + (i << 1)
    return res
"-----------------"
test()

