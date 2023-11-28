
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [2, [2, 4, 1]]
    # output: 2
    # EXPLANATION:  Buy on day 1 (price = 2) and sell on day 2 (price = 4), profit = 4-2 = 2.
    ,
    # example 2
    [2, [3, 2, 6, 5, 0, 3]]
    # output: 7
    # EXPLANATION:  Buy on day 2 (price = 2) and sell on day 3 (price = 6), profit = 6-2 = 4. Then buy on day 5 (price = 0) and sell on day 6 (price = 3), profit = 3-0 = 3.
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
def f_gold(k: int, prices: List[int]) -> int:
    n = len(prices)
    if n < 2:
        return 0
    dp = [[[0] * 2 for _ in range(k + 1)] for _ in range(n)]
    for i in range(1, k + 1):
        dp[0][i][1] = -prices[0]
    for i in range(1, n):
        for j in range(1, k + 1):
            dp[i][j][0] = max(dp[i - 1][j][1] + prices[i], dp[i - 1][j][0])
            dp[i][j][1] = max(dp[i - 1][j - 1][0] - prices[i], dp[i - 1][j][1])
    return dp[-1][k][0]
"-----------------"
test()

