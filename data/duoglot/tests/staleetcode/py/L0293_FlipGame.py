
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    ["++++"]
    # output: ["--++","+--+","++--"]
    ,
    # example 2
    ["+"]
    # output: []
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
### generatePossibleNextMoves 
from typing import *
def f_gold(s: str) -> List[str]:
    if not s or len(s) < 2:
        return []
    n = len(s)
    res = []
    for i in range(n - 1):
        if s[i] == '+' and s[i + 1] == '+':
            res.append(s[:i] + "--" + s[i + 2 :])
    return res
"-----------------"
test()

