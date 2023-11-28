
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [[1, 2], [-2, -1], [-1, 2], [0, 2]]
    # output: 2
    # EXPLANATION:  The two tuples are: 1. (0, 0, 0, 1) -> nums1[0] + nums2[0] + nums3[0] + nums4[1] = 1 + (-2) + (-1) + 2 = 0 2. (1, 1, 0, 0) -> nums1[1] + nums2[1] + nums3[0] + nums4[0] = 2 + (-1) + (-1) + 0 = 0
    ,
    # example 2
    [[0], [0], [0], [0]]
    # output: 1
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
### fourSumCount 
from collections import Counter
from typing import *
def f_gold(nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]
) -> int:
    counter = Counter()
    for a in nums1:
        for b in nums2:
            counter[a + b] += 1
    ans = 0
    for c in nums3:
        for d in nums4:
            ans += counter[-(c + d)]
    return ans
"-----------------"
test()

