
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [[1, -3, 4], 1, 6]
    # output: 2
    # EXPLANATION:  The possible hidden sequences are: - [3, 4, 1, 5] - [4, 5, 2, 6] Thus, we return 2.
    ,
    # example 2
    [[3, -4, 5, 1, -2], -4, 5]
    # output: 4
    # EXPLANATION:  The possible hidden sequences are: - [-3, 0, -4, 1, 2, 0] - [-2, 1, -3, 2, 3, 1] - [-1, 2, -2, 3, 4, 2] - [0, 3, -1, 4, 5, 3] Thus, we return 4.
    ,
    # example 3
    [[4, -7, 2], 3, 6]
    # output: 0
    # EXPLANATION:  There are no possible hidden sequences. Thus, we return 0.
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
### numberOfArrays 
from typing import *
def f_gold(differences: List[int], lower: int, upper: int) -> int:
    num = mi = mx = 0
    for d in differences:
        num += d
        mi = min(mi, num)
        mx = max(mx, num)
    return max(0, upper - lower - (mx - mi) + 1)
"-----------------"
test()

