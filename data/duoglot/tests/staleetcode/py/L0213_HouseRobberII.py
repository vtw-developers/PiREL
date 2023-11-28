
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [[2, 3, 2]]
    # output: 3
    # EXPLANATION:  You cannot rob house 1 (money = 2) and then rob house 3 (money = 2), because they are adjacent houses.
    ,
    # example 2
    [[1, 2, 3, 1]]
    # output: 4
    # EXPLANATION:  Rob house 1 (money = 1) and then rob house 3 (money = 3). Total amount you can rob = 1 + 3 = 4.
    ,
    # example 3
    [[1, 2, 3]]
    # output: 3
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
### rob 
from typing import *
def f_gold(nums: List[int]) -> int:
    def f_goldRange(nums, l, r):
        a, b = 0, nums[l]
        for num in nums[l + 1 : r + 1]:
            a, b = b, max(num + a, b)
        return b
    n = len(nums)
    if n == 1:
        return nums[0]
    s1, s2 = f_goldRange(nums, 0, n - 2), f_goldRange(nums, 1, n - 1)
    return max(s1, s2)
"-----------------"
test()

