
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [1, 4]
    # output: 2
    # EXPLANATION:  1   (0 0 0 1) 4   (0 1 0 0)              The above arrows point to positions where the corresponding bits are different.
    ,
    # example 2
    [3, 1]
    # output: 1
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
### hammingDistance 
from typing import *
def f_gold(x: int, y: int) -> int:
    num, count = x ^ y, 0
    while num != 0:
        num &= num - 1
        count += 1
    return count
"-----------------"
test()

