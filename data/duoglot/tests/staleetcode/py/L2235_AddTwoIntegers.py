
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [12, 5]
    # output: 17
    # EXPLANATION:  num1 is 12, num2 is 5, and their sum is 12 + 5 = 17, so 17 is returned.
    ,
    # example 2
    [-10, 4]
    # output: -6
    # EXPLANATION:  num1 + num2 = -6, so -6 is returned.
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
### sum 
from typing import *
def f_gold(num1: int, num2: int) -> int:
    return num1 + num2
"-----------------"
test()

