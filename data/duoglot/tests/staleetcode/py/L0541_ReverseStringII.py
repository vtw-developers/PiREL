
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    ["abcdefg", 2]
    # output: "bacdfeg"
    ,
    # example 2
    ["abcd", 2]
    # output: "bacd"
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
### reverseStr 
from typing import *
def f_gold(s: str, k: int) -> str:
    t = list(s)
    for i in range(0, len(t), k << 1):
        t[i : i + k] = reversed(t[i : i + k])
    return ''.join(t)
"-----------------"
test()

