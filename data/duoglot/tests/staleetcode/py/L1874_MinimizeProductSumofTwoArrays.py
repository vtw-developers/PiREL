
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [[5, 3, 4, 2], [4, 2, 2, 5]]
    # output: 40
    # EXPLANATION:  We can rearrange nums1 to become [3,5,4,2]. The product sum of [3,5,4,2] and [4,2,2,5] is 3*4 + 5*2 + 4*2 + 2*5 = 40.
    ,
    # example 2
    [[2, 1, 4, 5, 7], [3, 2, 4, 8, 6]]
    # output: 65
    # EXPLANATION: We can rearrange nums1 to become [5,7,4,1,2]. The product sum of [5,7,4,1,2] and [3,2,4,8,6] is 5*3 + 7*2 + 4*4 + 1*8 + 2*6 = 65.
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
### minProductSum 
from typing import *
def f_gold(nums1: List[int], nums2: List[int]) -> int:
    nums1.sort()
    nums2.sort()
    n, res = len(nums1), 0
    for i in range(n):
        res += nums1[i] * nums2[n - i - 1]
    return res
"-----------------"
test()

