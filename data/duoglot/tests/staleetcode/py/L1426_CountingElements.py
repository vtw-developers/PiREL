
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [[1, 2, 3]]
    # output: 2
    # EXPLANATION:  1 and 2 are counted cause 2 and 3 are in arr.
    ,
    # example 2
    [[1, 1, 3, 3, 5, 5, 7, 7]]
    # output: 0
    # EXPLANATION:  No numbers are counted, cause there is no 2, 4, 6, or 8 in arr.
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
### countElements 
from typing import *
def f_gold(arr: List[int]) -> int:
    s = set(arr)
    res = 0
    for num in arr:
        if num + 1 in s:
            res += 1
    return res
"-----------------"
test()

