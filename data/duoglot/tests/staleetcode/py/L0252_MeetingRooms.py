
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [[[0, 30], [5, 10], [15, 20]]]
    # output: false
    ,
    # example 2
    [[[7, 10], [2, 4]]]
    # output: true
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
### canAttendMeetings 
from typing import *
def f_gold(intervals: List[List[int]]) -> bool:
    intervals.sort(key=lambda x: x[0])
    for i in range(len(intervals) - 1):
        if intervals[i][1] > intervals[i + 1][0]:
            return False
    return True
"-----------------"
test()

