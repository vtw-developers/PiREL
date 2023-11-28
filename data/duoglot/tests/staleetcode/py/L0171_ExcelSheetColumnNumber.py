
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    ["A"]
    # output: 1
    ,
    # example 2
    ["AB"]
    # output: 28
    ,
    # example 3
    ["ZY"]
    # output: 701
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
### titleToNumber 
from typing import *
def f_gold(columnTitle: str) -> int:
    res = 0
    for c in columnTitle:
        res = res * 26 + (ord(c) - ord('A') + 1)
    return res
"-----------------"
test()

