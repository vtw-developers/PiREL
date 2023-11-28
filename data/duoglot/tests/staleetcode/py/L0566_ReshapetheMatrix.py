
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [[[1, 2], [3, 4]], 1, 4]
    # output: [[1,2,3,4]]
    ,
    # example 2
    [[[1, 2], [3, 4]], 2, 4]
    # output: [[1,2],[3,4]]
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
### matrixReshape 
from typing import *
def f_gold(nums: List[List[int]], r: int, c: int) -> List[List[int]]:
    m, n = len(nums), len(nums[0])
    if m * n != r * c:
        return nums
    res = [[0] * c for _ in range(r)]
    for x in range(m * n):
        res[x // c][x % c] = nums[x // n][x % n]
    return res
"-----------------"
test()

