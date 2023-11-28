
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [[2, 5, 3, 4, 1]]
    # output: 3
    # EXPLANATION:  We can form three teams given the conditions. (2,3,4), (5,4,1), (5,3,1).
    ,
    # example 2
    [[2, 1, 3]]
    # output: 0
    # EXPLANATION:  We can't form any team given the conditions.
    ,
    # example 3
    [[1, 2, 3, 4]]
    # output: 4
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
### numTeams 
from typing import *
def f_gold(rating: List[int]) -> int:
    n, ans = len(rating), 0
    for j in range(1, n - 1):
        ia = ib = ka = kb = 0
        for i in range(j):
            if rating[i] < rating[j]:
                ia += 1
            elif rating[i] > rating[j]:
                ib += 1
        for k in range(j + 1, n):
            if rating[j] < rating[k]:
                ka += 1
            elif rating[j] > rating[k]:
                kb += 1
        ans += ia * ka + ib * kb
    return ans
"-----------------"
test()

