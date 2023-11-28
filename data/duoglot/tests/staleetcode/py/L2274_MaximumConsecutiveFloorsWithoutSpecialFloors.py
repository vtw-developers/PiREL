
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [2, 9, [4, 6]]
    # output: 3
    # EXPLANATION:  The following are the ranges (inclusive) of consecutive floors without a special floor: - (2, 3) with a total amount of 2 floors. - (5, 5) with a total amount of 1 floor. - (7, 9) with a total amount of 3 floors. Therefore, we return the maximum number which is 3 floors.
    ,
    # example 2
    [6, 8, [7, 6, 8]]
    # output: 0
    # EXPLANATION:  Every floor rented is a special floor, so we return 0.
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
### maxConsecutive 
from typing import *
def f_gold(bottom: int, top: int, special: List[int]) -> int:
    special.sort()
    ans = max(special[0] - bottom, top - special[-1])
    for i in range(1, len(special)):
        ans = max(ans, special[i] - special[i - 1] - 1)
    return ans
"-----------------"
test()

