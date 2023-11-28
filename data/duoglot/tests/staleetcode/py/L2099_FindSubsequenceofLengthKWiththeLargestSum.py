
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [[2, 1, 3, 3], 2]
    # output: [3,3]
    # EXPLANATION:  The subsequence has the largest sum of 3 + 3 = 6.
    ,
    # example 2
    [[-1, -2, 3, 4], 3]
    # output: [-1,3,4]
    # EXPLANATION:   The subsequence has the largest sum of -1 + 3 + 4 = 6.
    ,
    # example 3
    [[3, 4, 3, 3], 2]
    # output: [3,4]
    # EXPLANATION:  The subsequence has the largest sum of 3 + 4 = 7.  Another possible subsequence is [4, 3].
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
### maxSubsequence 
from typing import *
def f_gold(nums: List[int], k: int) -> List[int]:
    idx = list(range(len(nums)))
    idx.sort(key=lambda i: nums[i])
    return [nums[i] for i in sorted(idx[-k:])]
"-----------------"
test()

