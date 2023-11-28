
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [1, 2]
    # output: 3
    ,
    # example 2
    [2, 3]
    # output: 5
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
### getSum 
from typing import *
def f_gold(a: int, b: int) -> int:
    a, b = a & 0xFFFFFFFF, b & 0xFFFFFFFF
    while b:
        carry = ((a & b) << 1) & 0xFFFFFFFF
        a, b = a ^ b, carry
    return a if a < 0x80000000 else ~(a ^ 0xFFFFFFFF)
"-----------------"
test()

