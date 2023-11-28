
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [[1, 2, 2, 4]]
    # output: [2,3]
    ,
    # example 2
    [[1, 1]]
    # output: [1,2]
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
### findErrorNums 
from typing import *
def f_gold(nums: List[int]) -> List[int]:
    eor, n = 0, len(nums)
    for i in range(1, n + 1):
        eor ^= i ^ nums[i - 1]
    diff = eor & (~eor + 1)
    a = 0
    for i in range(1, n + 1):
        if (nums[i - 1] & diff) == 0:
            a ^= nums[i - 1]
        if (i & diff) == 0:
            a ^= i
    b = eor ^ a
    for num in nums:
        if a == num:
            return [a, b]
    return [b, a]
"-----------------"
test()

