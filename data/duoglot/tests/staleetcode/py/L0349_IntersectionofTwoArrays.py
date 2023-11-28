
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [[1, 2, 2, 1], [2, 2]]
    # output: [2]
    ,
    # example 2
    [[4, 9, 5], [9, 4, 9, 8, 4]]
    # output: [9,4]
    # EXPLANATION:  [4,9] is also accepted.
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
### intersection 
from typing import *
def f_gold(nums1: List[int], nums2: List[int]) -> List[int]:
    s = set(nums1)
    res = set()
    for num in nums2:
        if num in s:
            res.add(num)
    return list(res)
"-----------------"
test()

