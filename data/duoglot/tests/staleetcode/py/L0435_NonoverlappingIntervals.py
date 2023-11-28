
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [[[1, 2], [2, 3], [3, 4], [1, 3]]]
    # output: 1
    # EXPLANATION:  [1,3] can be removed and the rest of the intervals are non-overlapping.
    ,
    # example 2
    [[[1, 2], [1, 2], [1, 2]]]
    # output: 2
    # EXPLANATION:  You need to remove two [1,2] to make the rest of the intervals non-overlapping.
    ,
    # example 3
    [[[1, 2], [2, 3]]]
    # output: 0
    # EXPLANATION:  You don't need to remove any of the intervals since they're already non-overlapping.
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
### eraseOverlapIntervals 
from typing import *
def f_gold(intervals: List[List[int]]) -> int:
    intervals.sort(key=lambda x: x[1])
    ans, t = 0, intervals[0][1]
    for s, e in intervals[1:]:
        if s >= t:
            t = e
        else:
            ans += 1
    return ans
"-----------------"
test()

