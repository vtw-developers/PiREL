
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [[1, 2, 3, 4, 5, 6], [1, 1, 2, 2, 2, 2]]
    # output: 3
    # EXPLANATION:  You can make the sums of nums1 and nums2 equal with 3 operations. All indices are 0-indexed. - Change nums2[0] to 6. nums1 = [1,2,3,4,5,6], nums2 = [<u><strong>6</strong></u>,1,2,2,2,2]. - Change nums1[5] to 1. nums1 = [1,2,3,4,5,<strong><u>1</u></strong>], nums2 = [6,1,2,2,2,2]. - Change nums1[2] to 2. nums1 = [1,2,<strong><u>2</u></strong>,4,5,1], nums2 = [6,1,2,2,2,2].
    ,
    # example 2
    [[1, 1, 1, 1, 1, 1, 1], [6]]
    # output: -1
    # EXPLANATION:  There is no way to decrease the sum of nums1 or to increase the sum of nums2 to make them equal.
    ,
    # example 3
    [[6, 6], [1]]
    # output: 3
    # EXPLANATION:  You can make the sums of nums1 and nums2 equal with 3 operations. All indices are 0-indexed.  - Change nums1[0] to 2. nums1 = [<strong><u>2</u></strong>,6], nums2 = [1]. - Change nums1[1] to 2. nums1 = [2,<strong><u>2</u></strong>], nums2 = [1]. - Change nums2[0] to 4. nums1 = [2,2], nums2 = [<strong><u>4</u></strong>].
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
### minOperations 
from typing import *
def f_gold(nums1: List[int], nums2: List[int]) -> int:
    s1, s2 = sum(nums1), sum(nums2)
    if s1 == s2:
        return 0
    if s1 > s2:
        return f_gold(nums2, nums1)
    freq = [0] * 6
    for x in nums1:
        freq[6 - x] += 1
    for x in nums2:
        freq[x - 1] += 1
    diff = s2 - s1
    ans, i = 0, 5
    while i > 0 and diff > 0:
        while freq[i] and diff > 0:
            diff -= i
            freq[i] -= 1
            ans += 1
        i -= 1
    return -1 if diff > 0 else ans
"-----------------"
test()

