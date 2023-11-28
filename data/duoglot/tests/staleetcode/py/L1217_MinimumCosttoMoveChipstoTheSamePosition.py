
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [[1, 2, 3]]
    # output: 1
    # EXPLANATION:  First step: Move the chip at position 3 to position 1 with cost = 0. Second step: Move the chip at position 2 to position 1 with cost = 1. Total cost is 1.
    ,
    # example 2
    [[2, 2, 2, 3, 3]]
    # output: 2
    # EXPLANATION:  We can move the two chips at position  3 to position 2. Each move has cost = 1. The total cost = 2.
    ,
    # example 3
    [[1, 1000000000]]
    # output: 1
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
### minCostToMoveChips 
from typing import *
def f_gold(position: List[int]) -> int:
    a = sum(p % 2 for p in position)
    b = len(position) - a
    return min(a, b)
"-----------------"
test()

