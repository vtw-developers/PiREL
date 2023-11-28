
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [[2, 2, 1]]
    # output: 1
    ,
    # example 2
    [[4, 1, 2, 1, 2]]
    # output: 4
    ,
    # example 3
    [[1]]
    # output: 1
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
    res = 0
    for num in nums:
        res ^= num
    return res
"-----------------"
test()

