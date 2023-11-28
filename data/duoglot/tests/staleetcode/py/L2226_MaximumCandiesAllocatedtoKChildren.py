
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [[5, 8, 6], 3]
    # output: 5
    # EXPLANATION:  We can divide candies[1] into 2 piles of size 5 and 3, and candies[2] into 2 piles of size 5 and 1. We now have five piles of candies of sizes 5, 5, 3, 5, and 1. We can allocate the 3 piles of size 5 to 3 children. It can be proven that each child cannot receive more than 5 candies.
    ,
    # example 2
    [[2, 5], 11]
    # output: 0
    # EXPLANATION:  There are 11 children but only 7 candies in total, so it is impossible to ensure each child receives at least one candy. Thus, each child gets no candy and the answer is 0.
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
### maximumCandies 
from typing import *
def f_gold(candies: List[int], k: int) -> int:
    left, right = 0, max(candies)
    while left < right:
        mid = (left + right + 1) >> 1
        cnt = sum(v // mid for v in candies)
        if cnt >= k:
            left = mid
        else:
            right = mid - 1
    return left
"-----------------"
test()

