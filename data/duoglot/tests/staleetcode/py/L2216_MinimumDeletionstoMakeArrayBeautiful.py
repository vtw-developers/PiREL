
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [[1, 1, 2, 3, 5]]
    # output: 1
    # EXPLANATION:  You can delete either <code>nums[0]</code> or <code>nums[1]</code> to make <code>nums</code> = [1,2,3,5] which is beautiful. It can be proven you need at least 1 deletion to make <code>nums</code> beautiful.
    ,
    # example 2
    [[1, 1, 2, 2, 3, 3]]
    # output: 2
    # EXPLANATION:  You can delete <code>nums[0]</code> and <code>nums[5]</code> to make nums = [1,2,2,3] which is beautiful. It can be proven you need at least 2 deletions to make nums beautiful.
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
### minDeletion 
from typing import *
def f_gold(nums: List[int]) -> int:
    n = len(nums)
    i = ans = 0
    while i < n - 1:
        if nums[i] == nums[i + 1]:
            ans += 1
            i += 1
        else:
            i += 2
    if (n - ans) % 2:
        ans += 1
    return ans
"-----------------"
test()

