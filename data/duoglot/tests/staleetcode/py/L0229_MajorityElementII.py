
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [[3, 2, 3]]
    # output: [3]
    ,
    # example 2
    [[1]]
    # output: [1]
    ,
    # example 3
    [[1, 2]]
    # output: [1,2]
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
def f_gold(nums: List[int]) -> List[int]:
    n1 = n2 = 0
    m1, m2 = 0, 1
    for m in nums:
        if m == m1:
            n1 += 1
        elif m == m2:
            n2 += 1
        elif n1 == 0:
            m1, n1 = m, 1
        elif n2 == 0:
            m2, n2 = m, 1
        else:
            n1, n2 = n1 - 1, n2 - 1
    return [m for m in [m1, m2] if nums.count(m) > len(nums) // 3]
"-----------------"
test()

