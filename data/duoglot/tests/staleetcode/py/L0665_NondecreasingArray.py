
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [[4, 2, 3]]
    # output: true
    # EXPLANATION:  You could modify the first <code>4</code> to <code>1</code> to get a non-decreasing array.
    ,
    # example 2
    [[4, 2, 1]]
    # output: false
    # EXPLANATION:  You can't get a non-decreasing array by modify at most one element.
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
### checkPossibility 
from typing import *
def f_gold(nums):
    """
    :type nums: List[int]
    :rtype: bool
    """
    if len(nums) < 2:
        return True
    count = 0
    for i in range(1, len(nums)):
        if nums[i] < nums[i - 1]:
            if count == 1:
                return False
            if not (
                i + 1 == len(nums)
                or nums[i + 1] >= nums[i - 1]
                or i - 2 < 0
                or nums[i - 2] < nums[i]
            ):
                return False
            else:
                count = 1
    return True
"-----------------"
test()

