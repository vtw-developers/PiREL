
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [[[0, 30], [5, 10], [15, 20]]]
    # output: 2
    ,
    # example 2
    [[[7, 10], [2, 4]]]
    # output: 1
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
### minMeetingRooms 
from itertools import accumulate
from typing import *
def f_gold(intervals: List[List[int]]) -> int:
    delta = [0] * 1000010
    for start, end in intervals:
        delta[start] += 1
        delta[end] -= 1
    return max(accumulate(delta))
"-----------------"
test()

