
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [[1, 3, 2, 8, 4, 9], 2]
    # output: 8
    # EXPLANATION:  The maximum profit can be achieved by: - Buying at prices[0] = 1 - Selling at prices[3] = 8 - Buying at prices[4] = 4 - Selling at prices[5] = 9 The total profit is ((8 - 1) - 2) + ((9 - 4) - 2) = 8.
    ,
    # example 2
    [[1, 3, 7, 5, 10, 3], 3]
    # output: 6
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
### maxProfit 
from typing import *
def f_gold(prices: List[int], fee: int) -> int:
    f1, f2 = -prices[0], 0
    for price in prices[1:]:
        f1 = max(f1, f2 - price)
        f2 = max(f2, f1 + price - fee)
    return f2
"-----------------"
test()

