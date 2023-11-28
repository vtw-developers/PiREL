
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [[4, 1, 6, 5]]
    # output: 4
    # EXPLANATION:   - We remove 1 bean from the bag with only 1 bean.   This results in the remaining bags: [4,<b><u>0</u></b>,6,5] - Then we remove 2 beans from the bag with 6 beans.   This results in the remaining bags: [4,0,<strong><u>4</u></strong>,5] - Then we remove 1 bean from the bag with 5 beans.   This results in the remaining bags: [4,0,4,<b><u>4</u></b>] We removed a total of 1 + 2 + 1 = 4 beans to make the remaining non-empty bags have an equal number of beans. There are no other solutions that remove 4 beans or fewer.
    ,
    # example 2
    [[2, 10, 3, 2]]
    # output: 7
    # EXPLANATION:  - We remove 2 beans from one of the bags with 2 beans.   This results in the remaining bags: [<u><strong>0</strong></u>,10,3,2] - Then we remove 2 beans from the other bag with 2 beans.   This results in the remaining bags: [0,10,3,<u><strong>0</strong></u>] - Then we remove 3 beans from the bag with 3 beans.    This results in the remaining bags: [0,10,<u><strong>0</strong></u>,0] We removed a total of 2 + 2 + 3 = 7 beans to make the remaining non-empty bags have an equal number of beans. There are no other solutions that removes 7 beans or fewer.
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
### minimumRemoval 
from typing import *
def f_gold(beans: List[int]) -> int:
    beans.sort()
    ans = s = sum(beans)
    n = len(beans)
    for i, v in enumerate(beans):
        ans = min(ans, s - v * (n - i))
    return ans
"-----------------"
test()

