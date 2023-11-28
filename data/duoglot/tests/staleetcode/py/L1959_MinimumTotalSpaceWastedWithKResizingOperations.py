
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [[10, 20], 0]
    # output: 10
    # EXPLANATION:  size = [20,20]. We can set the initial size to be 20. The total wasted space is (20 - 10) + (20 - 20) = 10.
    ,
    # example 2
    [[10, 20, 30], 1]
    # output: 10
    # EXPLANATION:  size = [20,20,30]. We can set the initial size to be 20 and resize to 30 at time 2.  The total wasted space is (20 - 10) + (20 - 20) + (30 - 30) = 10.
    ,
    # example 3
    [[10, 20, 15, 30, 20], 2]
    # output: 15
    # EXPLANATION:  size = [10,20,20,30,30]. We can set the initial size to 10, resize to 20 at time 1, and resize to 30 at time 3. The total wasted space is (10 - 10) + (20 - 20) + (20 - 15) + (30 - 30) + (30 - 20) = 15.
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
### minSpaceWastedKResizing 
import math
from math import inf
from typing import *
def f_gold(nums: List[int], k: int) -> int:
    k += 1
    n = len(nums)
    g = [[0] * n for _ in range(n)]
    for i in range(n):
        s = mx = 0
        for j in range(i, n):
            s += nums[j]
            mx = max(mx, nums[j])
            g[i][j] = mx * (j - i + 1) - s
    f = [[inf] * (k + 1) for _ in range(n + 1)]
    f[0][0] = 0
    for i in range(1, n + 1):
        for j in range(1, k + 1):
            for h in range(i):
                f[i][j] = min(f[i][j], f[h][j - 1] + g[h][i - 1])
    return f[-1][-1]
"-----------------"
test()

