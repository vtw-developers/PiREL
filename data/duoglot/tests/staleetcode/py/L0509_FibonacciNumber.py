
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [2]
    # output: 1
    # EXPLANATION:  F(2) = F(1) + F(0) = 1 + 0 = 1.
    ,
    # example 2
    [3]
    # output: 2
    # EXPLANATION:  F(3) = F(2) + F(1) = 1 + 1 = 2.
    ,
    # example 3
    [4]
    # output: 3
    # EXPLANATION:  F(4) = F(3) + F(2) = 2 + 1 = 3.
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
### fib 
from typing import *
def f_gold(n: int) -> int:
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a
"-----------------"
test()

