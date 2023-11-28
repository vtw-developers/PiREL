
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    ["Hello"]
    # output: "hello"
    ,
    # example 2
    ["here"]
    # output: "here"
    ,
    # example 3
    ["LOVELY"]
    # output: "lovely"
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
### toLowerCase 
from typing import *
def f_gold(s: str) -> str:
    return ''.join(
        [chr(ord(c) | 32) if ord('A') <= ord(c) <= ord('Z') else c for c in s]
    )
"-----------------"
test()

