
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    ["abbaca"]
    # output: "ca"
    # EXPLANATION:   For example, in "abbaca" we could remove "bb" since the letters are adjacent and equal, and this is the only possible move.  The result of this move is that the string is "aaca", of which only "aa" is possible, so the final string is "ca".
    ,
    # example 2
    ["azxxzy"]
    # output: "ay"
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
### removeDuplicates 
from typing import *
def f_gold(S: str) -> str:
    res = []
    for s in S:
        if not res or res[-1] != s:
            res.append(s)
        else:
            res.pop()
    return ''.join(res)
"-----------------"
test()

