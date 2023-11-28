
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [[3, 3, 5, 0, 0, 3, 1, 4]]
    # output: 6
    # EXPLANATION:  Buy on day 4 (price = 0) and sell on day 6 (price = 3), profit = 3-0 = 3. Then buy on day 7 (price = 1) and sell on day 8 (price = 4), profit = 4-1 = 3.
    ,
    # example 2
    [[1, 2, 3, 4, 5]]
    # output: 4
    # EXPLANATION:  Buy on day 1 (price = 1) and sell on day 5 (price = 5), profit = 5-1 = 4. Note that you cannot buy on day 1, buy on day 2 and sell them later, as you are engaging multiple transactions at the same time. You must sell before buying again.
    ,
    # example 3
    [[7, 6, 4, 3, 1]]
    # output: 0
    # EXPLANATION:  In this case, no transaction is done, i.e. max profit = 0.
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
def f_gold(prices: List[int]) -> int:
    f1, f2, f3, f4 = -prices[0], 0, -prices[0], 0
    for price in prices[1:]:
        f1 = max(f1, -price)
        f2 = max(f2, f1 + price)
        f3 = max(f3, f2 - price)
        f4 = max(f4, f3 + price)
    return f4
"-----------------"
test()

