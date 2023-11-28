
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [4]
    # output: 4
    # EXPLANATION:   T_3 = 0 + 1 + 1 = 2  T_4 = 1 + 1 + 2 = 4
    ,
    # example 2
    [25]
    # output: 1389537
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
### tribonacci 
from typing import *
def f_gold(n: int) -> int:
    a, b, c = 0, 1, 1
    for _ in range(n):
        a, b, c = b, c, a + b + c
    return a
"-----------------"
test()

