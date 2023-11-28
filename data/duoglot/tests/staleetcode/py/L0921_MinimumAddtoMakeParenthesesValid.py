
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    ["())"]
    # output: 1
    ,
    # example 2
    ["((("]
    # output: 3
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
### minAddToMakeValid 
from typing import *
def f_gold(s: str) -> int:
    stk = []
    for c in s:
        if c == '(':
            stk.append(c)
        else:
            if stk and stk[-1] == '(':
                stk.pop()
            else:
                stk.append(c)
    return len(stk)
"-----------------"
test()

