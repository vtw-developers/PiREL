
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [[1, 2, 2, 3]]
    # output: true
    ,
    # example 2
    [[6, 5, 4, 4]]
    # output: true
    ,
    # example 3
    [[1, 3, 2]]
    # output: false
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
### isMonotonic 
from typing import *
def f_gold(nums: List[int]) -> bool:
    isIncr = isDecr = False
    for i, v in enumerate(nums[1:]):
        if v < nums[i]:
            isIncr = True
        elif v > nums[i]:
            isDecr = True
        if isIncr and isDecr:
            return False
    return True
"-----------------"
test()

