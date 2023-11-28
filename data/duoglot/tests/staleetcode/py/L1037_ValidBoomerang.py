
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [[[1, 1], [2, 3], [3, 2]]]
    # output: true
    ,
    # example 2
    [[[1, 1], [2, 2], [3, 3]]]
    # output: false
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
### isBoomerang 
from typing import *
def f_gold(points: List[List[int]]) -> bool:
    (x1, y1), (x2, y2), (x3, y3) = points
    return (y2 - y1) * (x3 - x2) != (y3 - y2) * (x2 - x1)
"-----------------"
test()

