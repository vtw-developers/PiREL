
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [[7, 1, 5, 3, 6, 4]]
    # output: 5
    # EXPLANATION:  Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5. Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.
    ,
    # example 2
    [[7, 6, 4, 3, 1]]
    # output: 0
    # EXPLANATION:  In this case, no transactions are done and the max profit = 0.
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
    res, mi = 0, prices[0]
    for price in prices[1:]:
        res = max(res, price - mi)
        mi = min(mi, price)
    return res
"-----------------"
test()

