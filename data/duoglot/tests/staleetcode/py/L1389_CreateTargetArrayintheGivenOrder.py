
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [[0, 1, 2, 3, 4], [0, 1, 2, 2, 1]]
    # output: [0,4,1,3,2]
    # EXPLANATION:  nums       index     target 0            0        [0] 1            1        [0,1] 2            2        [0,1,2] 3            2        [0,1,3,2] 4            1        [0,4,1,3,2]
    ,
    # example 2
    [[1, 2, 3, 4, 0], [0, 1, 2, 3, 0]]
    # output: [0,1,2,3,4]
    # EXPLANATION:  nums       index     target 1            0        [1] 2            1        [1,2] 3            2        [1,2,3] 4            3        [1,2,3,4] 0            0        [0,1,2,3,4]
    ,
    # example 3
    [[1], [0]]
    # output: [1]
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
### createTargetArray 
from typing import *
def f_gold(nums: List[int], index: List[int]) -> List[int]:
    target = []
    for i in range(len(nums)):
        target.insert(index[i], nums[i])
    return target
"-----------------"
test()

