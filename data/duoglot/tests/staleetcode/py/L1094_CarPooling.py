
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [[[2, 1, 5], [3, 3, 7]], 4]
    # output: false
    ,
    # example 2
    [[[2, 1, 5], [3, 3, 7]], 5]
    # output: true
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
### carPooling 
from itertools import accumulate
from typing import *
def f_gold(trips: List[List[int]], capacity: int) -> bool:
    delta = [0] * 1001
    for num, start, end in trips:
        delta[start] += num
        delta[end] -= num
    return all(s <= capacity for s in accumulate(delta))
"-----------------"
test()

