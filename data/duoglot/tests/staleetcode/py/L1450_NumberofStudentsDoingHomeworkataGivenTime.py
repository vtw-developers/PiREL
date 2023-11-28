
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [[1, 2, 3], [3, 2, 7], 4]
    # output: 1
    # EXPLANATION:  We have 3 students where: The first student started doing homework at time 1 and finished at time 3 and wasn't doing anything at time 4. The second student started doing homework at time 2 and finished at time 2 and also wasn't doing anything at time 4. The third student started doing homework at time 3 and finished at time 7 and was the only student doing homework at time 4.
    ,
    # example 2
    [[4], [4], 4]
    # output: 1
    # EXPLANATION:  The only student was doing their homework at the queryTime.
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
### busyStudent 
from typing import *
def f_gold(startTime: List[int], endTime: List[int], queryTime: int
) -> int:
    count, n = 0, len(startTime)
    for i in range(n):
        count += startTime[i] <= queryTime <= endTime[i]
    return count
"-----------------"
test()

