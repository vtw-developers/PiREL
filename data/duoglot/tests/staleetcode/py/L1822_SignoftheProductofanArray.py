
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [[-1, -2, -3, -4, 3, 2, 1]]
    # output: 1
    # EXPLANATION:  The product of all values in the array is 144, and signFunc(144) = 1
    ,
    # example 2
    [[1, 5, 0, 2, -3]]
    # output: 0
    # EXPLANATION:  The product of all values in the array is 0, and signFunc(0) = 0
    ,
    # example 3
    [[-1, 1, -1, 1, -1]]
    # output: -1
    # EXPLANATION:  The product of all values in the array is -1, and signFunc(-1) = -1
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
### arraySign 
from typing import *
def f_gold(nums: List[int]) -> int:
    res = 1
    for num in nums:
        if num == 0:
            return 0
        if num < 0:
            res *= -1
    return res
"-----------------"
test()

