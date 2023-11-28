
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [[1, 2, 2, 6, 6, 6, 6, 7, 10]]
    # output: 6
    ,
    # example 2
    [[1, 1]]
    # output: 1
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
### findSpecialInteger 
from typing import *
def f_gold(arr: List[int]) -> int:
    n = len(arr)
    for i, val in enumerate(arr):
        if val == arr[i + (n >> 2)]:
            return val
    return 0
"-----------------"
test()

