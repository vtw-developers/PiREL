
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [16]
    # output: true
    ,
    # example 2
    [5]
    # output: false
    ,
    # example 3
    [1]
    # output: true
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
### isPowerOfFour 
from typing import *
def f_gold(n: int) -> bool:
    return n > 0 and (n & (n - 1)) == 0 and (n & 0xAAAAAAAA) == 0
"-----------------"
test()

