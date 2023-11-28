
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [[[1, 1], [3, 4], [-1, 0]]]
    # output: 7
    # EXPLANATION: One optimal path is <strong>[1,1]</strong> -> [2,2] -> [3,3] -> <strong>[3,4] </strong>-> [2,3] -> [1,2] -> [0,1] -> <strong>[-1,0]</strong>    Time from [1,1] to [3,4] = 3 seconds  Time from [3,4] to [-1,0] = 4 seconds Total time = 7 seconds
    ,
    # example 2
    [[[3, 2], [-2, 2]]]
    # output: 5
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
### minTimeToVisitAllPoints 
from typing import *
def f_gold(points: List[List[int]]) -> int:
    res = 0
    x0, y0 = points[0][0], points[0][1]
    for x1, y1 in points[1:]:
        res += max(abs(x0 - x1), abs(y0 - y1))
        x0, y0 = x1, y1
    return res
"-----------------"
test()

