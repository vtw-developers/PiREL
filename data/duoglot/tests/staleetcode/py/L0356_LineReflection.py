
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [[[1, 1], [-1, 1]]]
    # output: true
    # EXPLANATION:  We can choose the line x = 0.
    ,
    # example 2
    [[[1, 1], [-1, -1]]]
    # output: false
    # EXPLANATION:  We can't choose a line.
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
### isReflected 
import math
from math import inf
from typing import *
def f_gold(points: List[List[int]]) -> bool:
    min_x, max_x = float('inf'), float('-inf')
    point_set = set()
    for x, y in points:
        min_x = min(min_x, x)
        max_x = max(max_x, x)
        point_set.add((x, y))
    s = min_x + max_x
    for x, y in points:
        if (s - x, y) not in point_set:
            return False
    return True
"-----------------"
test()

