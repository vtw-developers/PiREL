
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [34, 6]
    # output: 9
    # EXPLANATION: 34 (base 10) expressed in base 6 is 54. 5 + 4 = 9.
    ,
    # example 2
    [10, 10]
    # output: 1
    # EXPLANATION: n is already in base 10. 1 + 0 = 1.
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
### sumBase 
from typing import *
def f_gold(n: int, k: int) -> int:
    res = 0
    while n != 0:
        n, t = divmod(n, k)
        res += t
    return res
"-----------------"
test()

