
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [[1, 1, 2, 2, 2, 3]]
    # output: [3,1,1,2,2,2]
    # EXPLANATION:  '3' has a frequency of 1, '1' has a frequency of 2, and '2' has a frequency of 3.
    ,
    # example 2
    [[2, 3, 1, 3, 2]]
    # output: [1,3,3,2,2]
    # EXPLANATION:  '2' and '3' both have a frequency of 2, so they are sorted in decreasing order.
    ,
    # example 3
    [[-1, 1, -6, 4, 5, -6, 1, 4, 1]]
    # output: [5,-1,4,4,-6,-6,1,1,1]
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
### frequencySort 
from collections import Counter
from typing import *
def f_gold(nums: List[int]) -> List[int]:
    cnt = Counter(nums)
    cnt = sorted(cnt.items(), key=lambda x: (x[1], -x[0]))
    ans = []
    for v, freq in cnt:
        ans.extend([v] * freq)
    return ans
"-----------------"
test()

