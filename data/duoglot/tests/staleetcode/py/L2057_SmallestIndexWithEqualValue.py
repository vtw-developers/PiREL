
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [[0, 1, 2]]
    # output: 0
    # EXPLANATION:   i=0: 0 mod 10 = 0 == nums[0]. i=1: 1 mod 10 = 1 == nums[1]. i=2: 2 mod 10 = 2 == nums[2]. All indices have i mod 10 == nums[i], so we return the smallest index 0.
    ,
    # example 2
    [[4, 3, 2, 1]]
    # output: 2
    # EXPLANATION:   i=0: 0 mod 10 = 0 != nums[0]. i=1: 1 mod 10 = 1 != nums[1]. i=2: 2 mod 10 = 2 == nums[2]. i=3: 3 mod 10 = 3 != nums[3]. 2 is the only index which has i mod 10 == nums[i].
    ,
    # example 3
    [[1, 2, 3, 4, 5, 6, 7, 8, 9, 0]]
    # output: -1
    # EXPLANATION:  No index satisfies i mod 10 == nums[i].
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
### smallestEqual 
from typing import *
def f_gold(nums: List[int]) -> int:
    for i, v in enumerate(nums):
        if i % 10 == v:
            return i
    return -1
"-----------------"
test()

