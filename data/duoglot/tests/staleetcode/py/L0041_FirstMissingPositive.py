
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [[1, 2, 0]]
    # output: 3
    ,
    # example 2
    [[3, 4, -1, 1]]
    # output: 2
    ,
    # example 3
    [[7, 8, 9, 11, 12]]
    # output: 1
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
### firstMissingPositive 
from typing import *
def f_gold(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    i = 1
    while i in nums:
        i += 1
    return i
"-----------------"
test()

