
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [1000, 15, 60]
    # output: 5
    ,
    # example 2
    [4, 15, 15]
    # output: 2
    ,
    # example 3
    [4, 15, 30]
    # output: 2
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
### poorPigs 
from typing import *
def f_gold(buckets: int, minutesToDie: int, minutesToTest: int) -> int:
    base = minutesToTest // minutesToDie + 1
    res, p = 0, 1
    while p < buckets:
        p *= base
        res += 1
    return res
"-----------------"
test()

