
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    ["11", "1"]
    # output: "100"
    ,
    # example 2
    ["1010", "1011"]
    # output: "10101"
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
### addBinary 
from typing import *
def f_gold(a: str, b: str) -> str:
    return bin(int(a, 2) + int(b, 2))[2:]
"-----------------"
test()

