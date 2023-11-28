
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    ["abcde", "cdeab"]
    # output: true
    ,
    # example 2
    ["abcde", "abced"]
    # output: false
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
### rotateString 
from typing import *
def f_gold(s: str, goal: str) -> bool:
    return len(s) == len(goal) and goal in s + s
"-----------------"
test()

