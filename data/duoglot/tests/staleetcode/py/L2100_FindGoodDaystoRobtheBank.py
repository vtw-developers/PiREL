
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [[5, 3, 3, 3, 5, 6, 2], 2]
    # output: [2,3]
    # EXPLANATION:  On day 2, we have security[0] >= security[1] >= security[2] <= security[3] <= security[4]. On day 3, we have security[1] >= security[2] >= security[3] <= security[4] <= security[5]. No other days satisfy this condition, so days 2 and 3 are the only good days to rob the bank.
    ,
    # example 2
    [[1, 1, 1, 1, 1], 0]
    # output: [0,1,2,3,4]
    # EXPLANATION:  Since time equals 0, every day is a good day to rob the bank, so return every day.
    ,
    # example 3
    [[1, 2, 3, 4, 5, 6], 2]
    # output: []
    # EXPLANATION:  No day has 2 days before it that have a non-increasing number of guards. Thus, no day is a good day to rob the bank, so return an empty list.
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
### goodDaysToRobBank 
from typing import *
def f_gold(security: List[int], time: int) -> List[int]:
    n = len(security)
    if n <= time * 2:
        return []
    left, right = [0] * n, [0] * n
    for i in range(1, n):
        if security[i] <= security[i - 1]:
            left[i] = left[i - 1] + 1
    for i in range(n - 2, -1, -1):
        if security[i] <= security[i + 1]:
            right[i] = right[i + 1] + 1
    return [i for i in range(n) if time <= min(left[i], right[i])]
"-----------------"
test()

