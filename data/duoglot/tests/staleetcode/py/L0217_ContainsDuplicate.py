
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [[1, 2, 3, 1]]
    # output: true
    ,
    # example 2
    [[1, 2, 3, 4]]
    # output: false
    ,
    # example 3
    [[1, 1, 1, 3, 3, 4, 3, 2, 4, 2]]
    # output: true
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
### containsDuplicate 
from typing import *
def f_gold(nums: List[int]) -> bool:
    return len(set(nums)) < len(nums)
"-----------------"
test()

