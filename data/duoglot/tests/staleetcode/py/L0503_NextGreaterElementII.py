
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [[1, 2, 1]]
    # output: [2,-1,2]
    # EXPLANATION:  The first 1's next greater number is 2;  The number 2 can't find next greater number.  The second 1's next greater number needs to search circularly, which is also 2.
    ,
    # example 2
    [[1, 2, 3, 4, 3]]
    # output: [2,3,4,-1,4]
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
### nextGreaterElements 
from typing import *
def f_gold(nums: List[int]) -> List[int]:
    n = len(nums)
    ans = [-1] * n
    stk = []
    for i in range(n << 1):
        while stk and nums[stk[-1]] < nums[i % n]:
            ans[stk.pop()] = nums[i % n]
        stk.append(i % n)
    return ans
"-----------------"
test()

