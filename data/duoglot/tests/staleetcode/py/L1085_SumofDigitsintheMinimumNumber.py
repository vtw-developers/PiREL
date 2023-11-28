
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [[34, 23, 1, 24, 75, 33, 54, 8]]
    # output: 0
    # EXPLANATION:  The minimal element is 1, and the sum of those digits is 1 which is odd, so the answer is 0.
    ,
    # example 2
    [[99, 77, 33, 66, 55]]
    # output: 1
    # EXPLANATION:  The minimal element is 33, and the sum of those digits is 3 + 3 = 6 which is even, so the answer is 1.
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
### sumOfDigits 
from typing import *
def f_gold(nums: List[int]) -> int:
    x = min(nums)
    s = 0
    while x:
        s += x % 10
        x //= 10
    return 0 if s % 2 else 1
"-----------------"
test()

