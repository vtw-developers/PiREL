
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [[1, 3], [2]]
    # output: 2.00000
    # EXPLANATION:  merged array = [1,2,3] and median is 2.
    ,
    # example 2
    [[1, 2], [3, 4]]
    # output: 2.50000
    # EXPLANATION:  merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
### findMedianSortedArrays 
import math
from math import inf
from typing import *
def f_gold(nums1: List[int], nums2: List[int]) -> float:
    def findKth(i, j, k):
        if i >= m:
            return nums2[j + k - 1]
        if j >= n:
            return nums1[i + k - 1]
        if k == 1:
            return min(nums1[i], nums2[j])
        midVal1 = nums1[i + k // 2 - 1] if i + k // 2 - 1 < m else float('inf')
        midVal2 = nums2[j + k // 2 - 1] if j + k // 2 - 1 < n else float('inf')
        if midVal1 < midVal2:
            return findKth(i + k // 2, j, k - k // 2)
        return findKth(i, j + k // 2, k - k // 2)
    m, n = len(nums1), len(nums2)
    left, right = (m + n + 1) // 2, (m + n + 2) // 2
    return (findKth(0, 0, left) + findKth(0, 0, right)) / 2
"-----------------"
test()

