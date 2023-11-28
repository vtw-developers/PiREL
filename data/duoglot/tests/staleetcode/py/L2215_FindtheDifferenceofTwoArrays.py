
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [[1, 2, 3], [2, 4, 6]]
    # output: [[1,3],[4,6]]
    # EXPLANATION: For nums1, nums1[1] = 2 is present at index 0 of nums2, whereas nums1[0] = 1 and nums1[2] = 3 are not present in nums2. Therefore, answer[0] = [1,3]. For nums2, nums2[0] = 2 is present at index 1 of nums1, whereas nums2[1] = 4 and nums2[2] = 6 are not present in nums2. Therefore, answer[1] = [4,6].
    ,
    # example 2
    [[1, 2, 3, 3], [1, 1, 2, 2]]
    # output: [[3],[]]
    # EXPLANATION: For nums1, nums1[2] and nums1[3] are not present in nums2. Since nums1[2] == nums1[3], their value is only included once and answer[0] = [3]. Every integer in nums2 is present in nums1. Therefore, answer[1] = [].
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
### findDifference 
from typing import *
def f_gold(nums1: List[int], nums2: List[int]) -> List[List[int]]:
    s1, s2 = set(nums1), set(nums2)
    return [list(s1 - s2), list(s2 - s1)]
"-----------------"
test()

