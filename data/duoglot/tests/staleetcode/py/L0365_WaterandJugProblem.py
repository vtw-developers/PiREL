
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [3, 5, 4]
    # output: true
    # EXPLANATION:  The famous <a href="https://www.youtube.com/watch?v=BVtQNK_ZUJg&ab_channel=notnek01" target="_blank">Die Hard</a> example
    ,
    # example 2
    [2, 6, 5]
    # output: false
    ,
    # example 3
    [1, 2, 3]
    # output: true
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
### canMeasureWater 
import math
from math import gcd
from typing import *
def f_gold(jug1Capacity: int, jug2Capacity: int, targetCapacity: int
) -> bool:
    if jug1Capacity + jug2Capacity < targetCapacity:
        return False
    if jug1Capacity == 0 or jug2Capacity == 0:
        return targetCapacity == 0 or jug1Capacity + jug2Capacity == targetCapacity
    return targetCapacity % gcd(jug1Capacity, jug2Capacity) == 0
"-----------------"
test()

