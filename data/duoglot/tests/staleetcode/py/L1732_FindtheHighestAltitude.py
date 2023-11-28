
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [[-5, 1, 5, 0, -7]]
    # output: 1
    # EXPLANATION:  The altitudes are [0,-5,-4,1,1,-6]. The highest is 1.
    ,
    # example 2
    [[-4, -3, -2, -1, 4, 3, 2]]
    # output: 0
    # EXPLANATION:  The altitudes are [0,-4,-7,-9,-10,-6,-3,-1]. The highest is 0.
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
### largestAltitude 
from typing import *
def f_gold(gain: List[int]) -> int:
    res = t = 0
    for h in gain:
        t += h
        res = max(res, t)
    return res
"-----------------"
test()

