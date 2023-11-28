
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [[1, 8, 6, 2, 5, 4, 8, 3, 7]]
    # output: 49
    # EXPLANATION:  The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.
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
### maxArea 
from typing import *
def f_gold(height: List[int]) -> int:
    i, j = 0, len(height) - 1
    res = 0
    while i < j:
        t = (j - i) * min(height[i], height[j])
        res = max(res, t)
        if height[i] < height[j]:
            i += 1
        else:
            j -= 1
    return res
"-----------------"
test()

