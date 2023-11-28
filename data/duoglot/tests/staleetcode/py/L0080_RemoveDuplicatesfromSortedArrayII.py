
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [[1, 1, 1, 2, 2, 3]]
    # output: 5, nums = [1,1,2,2,3,_]
    # EXPLANATION:  Your function should return k = 5, with the first five elements of nums being 1, 1, 2, 2 and 3 respectively. It does not matter what you leave beyond the returned k (hence they are underscores).
    ,
    # example 2
    [[0, 0, 1, 1, 1, 1, 2, 3, 3]]
    # output: 7, nums = [0,0,1,1,2,3,3,_,_]
    # EXPLANATION:  Your function should return k = 7, with the first seven elements of nums being 0, 0, 1, 1, 2, 3 and 3 respectively. It does not matter what you leave beyond the returned k (hence they are underscores).
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
### removeDuplicates 
from typing import *
def f_gold(nums: List[int]) -> int:
    i = 0
    for num in nums:
        if i < 2 or num != nums[i - 2]:
            nums[i] = num
            i += 1
    return i
"-----------------"
test()

