
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [[60, 60, 60], [10, 90, 10]]
    # output: 210
    # EXPLANATION:  Choosing left = 1 and right = 1, we have nums1 = [60,<u><strong>90</strong></u>,60] and nums2 = [10,<u><strong>60</strong></u>,10]. The score is max(sum(nums1), sum(nums2)) = max(210, 80) = 210.
    ,
    # example 2
    [[20, 40, 20, 70, 30], [50, 20, 50, 40, 20]]
    # output: 220
    # EXPLANATION:  Choosing left = 3, right = 4, we have nums1 = [20,40,20,<u><strong>40,20</strong></u>] and nums2 = [50,20,50,<u><strong>70,30</strong></u>]. The score is max(sum(nums1), sum(nums2)) = max(140, 220) = 220.
    ,
    # example 3
    [[7, 11, 13], [1, 1, 1]]
    # output: 31
    # EXPLANATION:  We choose not to swap any subarray. The score is max(sum(nums1), sum(nums2)) = max(31, 3) = 31.
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
### maximumsSplicedArray 
from typing import *
def f_gold(nums1: List[int], nums2: List[int]) -> int:
    def f(nums1, nums2):
        d = [a - b for a, b in zip(nums1, nums2)]
        t = mx = d[0]
        for v in d[1:]:
            if t > 0:
                t += v
            else:
                t = v
            mx = max(mx, t)
        return mx
    s1, s2 = sum(nums1), sum(nums2)
    return max(s2 + f(nums1, nums2), s1 + f(nums2, nums1))
"-----------------"
test()

