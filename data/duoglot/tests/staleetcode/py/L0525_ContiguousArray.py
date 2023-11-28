
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [[0, 1]]
    # output: 2
    # EXPLANATION:  [0, 1] is the longest contiguous subarray with an equal number of 0 and 1.
    ,
    # example 2
    [[0, 1, 0]]
    # output: 2
    # EXPLANATION:  [0, 1] (or [1, 0]) is a longest contiguous subarray with equal number of 0 and 1.
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
### findMaxLength 
from typing import *
def f_gold(nums: List[int]) -> int:
    s = ans = 0
    mp = {0: -1}
    for i, v in enumerate(nums):
        s += 1 if v == 1 else -1
        if s in mp:
            ans = max(ans, i - mp[s])
        else:
            mp[s] = i
    return ans
"-----------------"
test()

