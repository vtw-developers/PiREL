
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [[3, 2, 1]]
    # output: 1
    # EXPLANATION:  The first distinct maximum is 3. The second distinct maximum is 2. The third distinct maximum is 1.
    ,
    # example 2
    [[1, 2]]
    # output: 2
    # EXPLANATION:  The first distinct maximum is 2. The second distinct maximum is 1. The third distinct maximum does not exist, so the maximum (2) is returned instead.
    ,
    # example 3
    [[2, 2, 3, 1]]
    # output: 1
    # EXPLANATION:  The first distinct maximum is 3. The second distinct maximum is 2 (both 2's are counted together since they have the same value). The third distinct maximum is 1.
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
### thirdMax 
import math
from math import inf
from typing import *
def f_gold(nums: List[int]) -> int:
    m1 = m2 = m3 = float('-inf')
    for num in nums:
        if num in [m1, m2, m3]:
            continue
        if num > m1:
            m3, m2, m1 = m2, m1, num
        elif num > m2:
            m3, m2 = m2, num
        elif num > m3:
            m3 = num
    return m3 if m3 != float('-inf') else m1
"-----------------"
test()

