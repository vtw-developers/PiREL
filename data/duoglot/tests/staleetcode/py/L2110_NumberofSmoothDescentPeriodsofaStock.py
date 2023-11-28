
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [[3, 2, 1, 4]]
    # output: 7
    # EXPLANATION:  There are 7 smooth descent periods: [3], [2], [1], [4], [3,2], [2,1], and [3,2,1] Note that a period with one day is a smooth descent period by the definition.
    ,
    # example 2
    [[8, 6, 7, 7]]
    # output: 4
    # EXPLANATION:  There are 4 smooth descent periods: [8], [6], [7], and [7] Note that [8,6] is not a smooth descent period as 8 - 6   1.
    ,
    # example 3
    [[1]]
    # output: 1
    # EXPLANATION:  There is 1 smooth descent period: [1]
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
### getDescentPeriods 
from typing import *
def f_gold(prices: List[int]) -> int:
    i, n = 0, len(prices)
    ans = 0
    while i < n:
        j = i
        while j + 1 < n and prices[j] - prices[j + 1] == 1:
            j += 1
        t = j - i + 1
        ans += t * (t + 1) // 2
        i = j + 1
    return ans
"-----------------"
test()

