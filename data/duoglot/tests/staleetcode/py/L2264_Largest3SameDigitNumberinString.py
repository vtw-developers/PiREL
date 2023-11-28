
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    ["6777133339"]
    # output: "777"
    # EXPLANATION:  There are two distinct good integers: "777" and "333". "777" is the largest, so we return "777".
    ,
    # example 2
    ["2300019"]
    # output: "000"
    # EXPLANATION:  "000" is the only good integer.
    ,
    # example 3
    ["42352338"]
    # output: ""
    # EXPLANATION:  No substring of length 3 consists of only one unique digit. Therefore, there are no good integers.
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
### largestGoodInteger 
from typing import *
def f_gold(num: str) -> str:
    for i in range(9, -1, -1):
        t = str(i) * 3
        if t in num:
            return t
    return ''
"-----------------"
test()

