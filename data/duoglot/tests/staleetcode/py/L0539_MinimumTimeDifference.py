
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [["23:59", "00:00"]]
    # output: 1
    ,
    # example 2
    [["00:00", "23:59", "00:00"]]
    # output: 0
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
### findMinDifference 
from typing import *
def f_gold(timePoints: List[str]) -> int:
    if len(timePoints) > 24 * 60:
        return 0
    mins = sorted(int(t[:2]) * 60 + int(t[3:]) for t in timePoints)
    mins.append(mins[0] + 24 * 60)
    res = mins[-1]
    for i in range(1, len(mins)):
        res = min(res, mins[i] - mins[i - 1])
    return res
"-----------------"
test()

