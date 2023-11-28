
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [[2, 2, 3, 2]]
    # output: 3
    ,
    # example 2
    [[0, 1, 0, 1, 0, 1, 99]]
    # output: 99
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
### singleNumber 
from typing import *
def f_gold(nums: List[int]) -> int:
    ans = 0
    for i in range(32):
        cnt = sum(num >> i & 1 for num in nums)
        if cnt % 3:
            if i == 31:
                ans -= 1 << i
            else:
                ans |= 1 << i
    return ans
"-----------------"
test()

