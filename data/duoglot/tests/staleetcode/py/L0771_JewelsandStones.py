
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    ["aA", "aAAbbbb"]
    # output: 3
    ,
    # example 2
    ["z", "ZZ"]
    # output: 0
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
### numJewelsInStones 
from typing import *
def f_gold(jewels: str, stones: str) -> int:
    s = set(jewels)
    return sum([1 for c in stones if c in s])
"-----------------"
test()

