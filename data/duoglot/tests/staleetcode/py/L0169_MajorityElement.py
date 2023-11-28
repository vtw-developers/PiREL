
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [[3, 2, 3]]
    # output: 3
    ,
    # example 2
    [[2, 2, 1, 1, 1, 2, 2]]
    # output: 2
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
### majorityElement 
from typing import *
def f_gold(nums: List[int]) -> int:
    cnt = m = 0
    for v in nums:
        if cnt == 0:
            m, cnt = v, 1
        else:
            cnt += 1 if m == v else -1
    return m
"-----------------"
test()

