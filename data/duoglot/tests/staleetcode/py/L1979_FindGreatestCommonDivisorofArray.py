
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [[2, 5, 6, 9, 10]]
    # output: 2
    # EXPLANATION:  The smallest number in nums is 2. The largest number in nums is 10. The greatest common divisor of 2 and 10 is 2.
    ,
    # example 2
    [[7, 5, 6, 8, 3]]
    # output: 1
    # EXPLANATION:  The smallest number in nums is 3. The largest number in nums is 8. The greatest common divisor of 3 and 8 is 1.
    ,
    # example 3
    [[3, 3]]
    # output: 3
    # EXPLANATION:  The smallest number in nums is 3. The largest number in nums is 3. The greatest common divisor of 3 and 3 is 3.
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
### findGCD 
import math
from math import gcd
from typing import *
def f_gold(nums: List[int]) -> int:
    return gcd(max(nums), min(nums))
"-----------------"
test()

