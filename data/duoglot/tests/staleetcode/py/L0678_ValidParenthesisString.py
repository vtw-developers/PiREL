
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    ["()"]
    # output: true
    ,
    # example 2
    ["(*)"]
    # output: true
    ,
    # example 3
    ["(*))"]
    # output: true
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
### checkValidString 
from typing import *
def f_gold(s: str) -> bool:
    n = len(s)
    left, asterisk = 0, 0
    for i in range(n):
        if s[i] == "(":
            left += 1
        elif s[i] == ")":
            if left > 0:
                left -= 1
            elif asterisk > 0:
                asterisk -= 1
            else:
                return False
        else:
            asterisk += 1
    right, asterisk = 0, 0
    for i in range(n - 1, -1, -1):
        if s[i] == ")":
            right += 1
        elif s[i] == "(":
            if right > 0:
                right -= 1
            elif asterisk > 0:
                asterisk -= 1
            else:
                return False
        else:
            asterisk += 1
    return True
"-----------------"
test()

