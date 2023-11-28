
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [[2, 3, 5]]
    # output: [4,3,5]
    # EXPLANATION:  Assuming the arrays are 0-indexed, then result[0] = |2-2| + |2-3| + |2-5| = 0 + 1 + 3 = 4, result[1] = |3-2| + |3-3| + |3-5| = 1 + 0 + 2 = 3, result[2] = |5-2| + |5-3| + |5-5| = 3 + 2 + 0 = 5.
    ,
    # example 2
    [[1, 4, 6, 8, 10]]
    # output: [24,15,13,15,21]
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
### getSumAbsoluteDifferences 
from typing import *
def f_gold(nums: List[int]) -> List[int]:
    n = len(nums)
    presum = [0] * (n + 1)
    for i in range(n):
        presum[i + 1] = presum[i] + nums[i]
    res = []
    for i, num in enumerate(nums):
        t = num * i - presum[i] + presum[n] - presum[i + 1] - num * (n - i - 1)
        res.append(t)
    return res
"-----------------"
test()

