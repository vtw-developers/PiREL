
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    ["Hello, my name is John"]
    # output: 5
    # EXPLANATION:  The five segments are ["Hello,", "my", "name", "is", "John"]
    ,
    # example 2
    ["Hello"]
    # output: 1
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
### countSegments 
from typing import *
def f_gold(s: str) -> int:
    res = 0
    for i in range(len(s)):
        if s[i] != ' ' and (i == 0 or s[i - 1] == ' '):
            res += 1
    return res
"-----------------"
test()

