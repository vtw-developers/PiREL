
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [526]
    # output: true
    # EXPLANATION:  Reverse num to get 625, then reverse 625 to get 526, which equals num.
    ,
    # example 2
    [1800]
    # output: false
    # EXPLANATION:  Reverse num to get 81, then reverse 81 to get 18, which does not equal num.
    ,
    # example 3
    [0]
    # output: true
    # EXPLANATION:  Reverse num to get 0, then reverse 0 to get 0, which equals num.
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
### isSameAfterReversals 
from typing import *
def f_gold(num: int) -> bool:
    return num == 0 or num % 10 != 0
"-----------------"
test()

