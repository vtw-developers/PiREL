
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [[0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]]
    # output: 6
    # EXPLANATION:  The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped.
    ,
    # example 2
    [[4, 2, 0, 3, 2, 5]]
    # output: 9
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
### trap 
from typing import *
def f_gold(height: List[int]) -> int:
    n = len(height)
    if n < 3:
        return 0
    lmx, rmx = [height[0]] * n, [height[n - 1]] * n
    for i in range(1, n):
        lmx[i] = max(lmx[i - 1], height[i])
        rmx[n - 1 - i] = max(rmx[n - i], height[n - 1 - i])
    res = 0
    for i in range(n):
        res += min(lmx[i], rmx[i]) - height[i]
    return res
"-----------------"
test()

