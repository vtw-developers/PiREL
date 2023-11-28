
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [1]
    # output: "A"
    ,
    # example 2
    [28]
    # output: "AB"
    ,
    # example 3
    [701]
    # output: "ZY"
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
### convertToTitle 
from typing import *
def f_gold(columnNumber: int) -> str:
    res = []
    while columnNumber:
        columnNumber -= 1
        res.append(chr(ord('A') + columnNumber % 26))
        columnNumber //= 26
    return ''.join(res[::-1])
"-----------------"
test()

