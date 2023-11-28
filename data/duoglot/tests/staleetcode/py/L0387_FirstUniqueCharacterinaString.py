
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    ["leetcode"]
    # output: 0
    ,
    # example 2
    ["loveleetcode"]
    # output: 2
    ,
    # example 3
    ["aabb"]
    # output: -1
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
### firstUniqChar 
from collections import Counter
from typing import *
def f_gold(s: str) -> int:
    counter = Counter(s)
    for i, c in enumerate(s):
        if counter[c] == 1:
            return i
    return -1
"-----------------"
test()

