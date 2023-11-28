
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [[8, 1, 5, 2, 6]]
    # output: 11
    # EXPLANATION:  i = 0, j = 2, values[i] + values[j] + i - j = 8 + 5 + 0 - 2 = 11
    ,
    # example 2
    [[1, 2]]
    # output: 2
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
### maxScoreSightseeingPair 
from typing import *
def f_gold(values: List[int]) -> int:
    res, mx = 0, values[0]
    for i in range(1, len(values)):
        res = max(res, values[i] - i + mx)
        mx = max(mx, values[i] + i)
    return res
"-----------------"
test()

