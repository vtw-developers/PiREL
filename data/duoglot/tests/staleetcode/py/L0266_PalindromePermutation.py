
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    ["code"]
    # output: false
    ,
    # example 2
    ["aab"]
    # output: true
    ,
    # example 3
    ["carerac"]
    # output: true
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
### canPermutePalindrome 
from collections import Counter
from typing import *
def f_gold(s: str) -> bool:
    counter = Counter(s)
    return sum(e % 2 for e in counter.values()) < 2
"-----------------"
test()

