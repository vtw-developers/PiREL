
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [[1, 3, 2], 6]
    # output: 1
    # EXPLANATION: At speed 1: - The first train ride takes 1/1 = 1 hour. - Since we are already at an integer hour, we depart immediately at the 1 hour mark. The second train takes 3/1 = 3 hours. - Since we are already at an integer hour, we depart immediately at the 4 hour mark. The third train takes 2/1 = 2 hours. - You will arrive at exactly the 6 hour mark.
    ,
    # example 2
    [[1, 3, 2], 2.7]
    # output: 3
    # EXPLANATION: At speed 3: - The first train ride takes 1/3 = 0.33333 hours. - Since we are not at an integer hour, we wait until the 1 hour mark to depart. The second train ride takes 3/3 = 1 hour. - Since we are already at an integer hour, we depart immediately at the 2 hour mark. The third train takes 2/3 = 0.66667 hours. - You will arrive at the 2.66667 hour mark.
    ,
    # example 3
    [[1, 3, 2], 1.9]
    # output: -1
    # EXPLANATION:  It is impossible because the earliest the third train can depart is at the 2 hour mark.
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
### minSpeedOnTime 
import math
from math import ceil
from typing import *
def f_gold(dist: List[int], hour: float) -> int:
    def arrive_on_time(speed):
        res = 0
        for i, d in enumerate(dist):
            res += (d / speed) if i == len(dist) - 1 else math.ceil(d / speed)
        return res <= hour
    left, right = 1, 10**7
    while left < right:
        mid = (left + right) >> 1
        if arrive_on_time(mid):
            right = mid
        else:
            left = mid + 1
    return left if arrive_on_time(left) else -1
"-----------------"
test()

