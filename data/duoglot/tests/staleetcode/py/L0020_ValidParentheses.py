
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
    ["()[]{}"]
    # output: true
    ,
    # example 3
    ["(]"]
    # output: false
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
### isValid 
from typing import *
def f_gold(s: str) -> bool:
    q = []
    parentheses = {'()', '[]', '{}'}
    for ch in s:
        if ch in '([{':
            q.append(ch)
        elif not q or q.pop() + ch not in parentheses:
            return False
    return not q
"-----------------"
test()

