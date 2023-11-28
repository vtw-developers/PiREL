
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [[[1, 2, 3], [3, 2, 1]]]
    # output: 6
    # EXPLANATION: <strong>:</strong> <code>1st customer has wealth = 1 + 2 + 3 = 6 </code><code>2nd customer has wealth = 3 + 2 + 1 = 6 </code>Both customers are considered the richest with a wealth of 6 each, so return 6.
    ,
    # example 2
    [[[1, 5], [7, 3], [3, 5]]]
    # output: 10
    # EXPLANATION: :  1st customer has wealth = 6 2nd customer has wealth = 10  3rd customer has wealth = 8 The 2nd customer is the richest with a wealth of 10.
    ,
    # example 3
    [[[2, 8, 7], [7, 1, 3], [1, 9, 5]]]
    # output: 17
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
### maximumWealth 
from typing import *
def f_gold(accounts: List[List[int]]) -> int:
    return max(sum(account) for account in accounts)
"-----------------"
test()

