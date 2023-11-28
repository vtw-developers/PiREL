
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [4]
    # output: [2,1,4,3]
    ,
    # example 2
    [5]
    # output: [3,1,2,5,4]
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
### beautifulArray 
from typing import *
def f_gold(n: int) -> List[int]:
    if n == 1:
        return [1]
    left = f_gold((n + 1) >> 1)
    right = f_gold(n >> 1)
    left = [x * 2 - 1 for x in left]
    right = [x * 2 for x in right]
    return left + right
"-----------------"
test()

