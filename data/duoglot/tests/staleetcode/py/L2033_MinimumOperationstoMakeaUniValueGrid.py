
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [[[2, 4], [6, 8]], 2]
    # output: 4
    # EXPLANATION:  We can make every element equal to 4 by doing the following:  - Add x to 2 once. - Subtract x from 6 once. - Subtract x from 8 twice. A total of 4 operations were used.
    ,
    # example 2
    [[[1, 5], [2, 3]], 1]
    # output: 5
    # EXPLANATION:  We can make every element equal to 3.
    ,
    # example 3
    [[[1, 2], [3, 4]], 2]
    # output: -1
    # EXPLANATION:  It is impossible to make every element equal.
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
### minOperations 
from typing import *
def f_gold(grid: List[List[int]], x: int) -> int:
    nums = []
    m, n = len(grid), len(grid[0])
    base = grid[0][0]
    for i in range(m):
        for j in range(n):
            if abs(grid[i][j] - base) % x != 0:
                return -1
            nums.append(grid[i][j])
    nums.sort()
    mid = nums[len(nums) >> 1]
    ans = 0
    for num in nums:
        ans += abs(num - mid) // x
    return ans
"-----------------"
test()

