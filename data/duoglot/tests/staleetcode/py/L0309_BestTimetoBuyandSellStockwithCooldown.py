
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [[1, 2, 3, 0, 2]]
    # output: 3
    # EXPLANATION:  transactions = [buy, sell, cooldown, buy, sell]
    ,
    # example 2
    [[1]]
    # output: 0
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
    f1, f2, f3 = -prices[0], 0, 0
    for price in prices[1:]:
        pf1, pf2, pf3 = f1, f2, f3
        f1 = max(pf1, pf3 - price)
        f2 = max(pf2, pf1 + price)
        f3 = max(pf3, pf2)
    return f2
"-----------------"
test()

