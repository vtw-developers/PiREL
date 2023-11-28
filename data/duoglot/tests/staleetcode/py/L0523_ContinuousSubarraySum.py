
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [[23, 2, 4, 6, 7], 6]
    # output: true
    # EXPLANATION:  [2, 4] is a continuous subarray of size 2 whose elements sum up to 6.
    ,
    # example 2
    [[23, 2, 6, 4, 7], 6]
    # output: true
    # EXPLANATION:  [23, 2, 6, 4, 7] is an continuous subarray of size 5 whose elements sum up to 42. 42 is a multiple of 6 because 42 = 7 * 6 and 7 is an integer.
    ,
    # example 3
    [[23, 2, 6, 4, 7], 13]
    # output: false
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
### checkSubarraySum 
from typing import *
def f_gold(nums: List[int], k: int) -> bool:
    s = 0
    mp = {0: -1}
    for i, v in enumerate(nums):
        s += v
        r = s % k
        if r in mp and i - mp[r] >= 2:
            return True
        if r not in mp:
            mp[r] = i
    return False
"-----------------"
test()

