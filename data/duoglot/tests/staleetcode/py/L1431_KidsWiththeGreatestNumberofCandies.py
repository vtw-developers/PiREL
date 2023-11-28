
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [[2, 3, 5, 1, 3], 3]
    # output: [true,true,true,false,true]
    # EXPLANATION:  If you give all extraCandies to: - Kid 1, they will have 2 + 3 = 5 candies, which is the greatest among the kids. - Kid 2, they will have 3 + 3 = 6 candies, which is the greatest among the kids. - Kid 3, they will have 5 + 3 = 8 candies, which is the greatest among the kids. - Kid 4, they will have 1 + 3 = 4 candies, which is not the greatest among the kids. - Kid 5, they will have 3 + 3 = 6 candies, which is the greatest among the kids.
    ,
    # example 2
    [[4, 2, 1, 1, 2], 1]
    # output: [true,false,false,false,false]
    # EXPLANATION:  There is only 1 extra candy. Kid 1 will always have the greatest number of candies, even if a different kid is given the extra candy.
    ,
    # example 3
    [[12, 1, 12], 10]
    # output: [true,false,true]
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
### kidsWithCandies 
from typing import *
def f_gold(candies: List[int], extraCandies: int) -> List[bool]:
    mx = max(candies)
    return [candy + extraCandies >= mx for candy in candies]
"-----------------"
test()

