
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [[1, 1, 3, 2], [2, 3], [3]]
    # output: [3,2]
    # EXPLANATION:  The values that are present in at least two arrays are: - 3, in all three arrays. - 2, in nums1 and nums2.
    ,
    # example 2
    [[3, 1], [2, 3], [1, 2]]
    # output: [2,3,1]
    # EXPLANATION:  The values that are present in at least two arrays are: - 2, in nums2 and nums3. - 3, in nums1 and nums2. - 1, in nums1 and nums3.
    ,
    # example 3
    [[1, 2, 2], [4, 3, 3], [5]]
    # output: []
    # EXPLANATION:  No value is present in at least two arrays.
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
### twoOutOfThree 
from typing import *
def f_gold(nums1: List[int], nums2: List[int], nums3: List[int]
) -> List[int]:
    s1, s2, s3 = set(nums1), set(nums2), set(nums3)
    ans = []
    for i in range(1, 101):
        a, b, c = i in s1, i in s2, i in s3
        if a + b + c > 1:
            ans.append(i)
    return ans
"-----------------"
test()

