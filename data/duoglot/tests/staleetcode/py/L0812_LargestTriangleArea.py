
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [[[0, 0], [0, 1], [1, 0], [0, 2], [2, 0]]]
    # output: 2.00000
    # EXPLANATION:  The five points are shown in the above figure. The red triangle is the largest.
    ,
    # example 2
    [[[1, 0], [0, 0], [0, 1]]]
    # output: 0.50000
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
### largestTriangleArea 
from typing import *
def f_gold(points: List[List[int]]) -> float:
    ans = 0
    for x1, y1 in points:
        for x2, y2 in points:
            for x3, y3 in points:
                u1, v1 = x2 - x1, y2 - y1
                u2, v2 = x3 - x1, y3 - y1
                t = abs(u1 * v2 - u2 * v1) / 2
                ans = max(ans, t)
    return ans
"-----------------"
test()

