
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [10]
    # output: 16
    # EXPLANATION:  The winning strategy is as follows: - The range is [1,10]. Guess 7.     - If this is my number, your total is $0. Otherwise, you pay $7.     - If my number is higher, the range is [8,10]. Guess 9.         - If this is my number, your total is $7. Otherwise, you pay $9.         - If my number is higher, it must be 10. Guess 10. Your total is $7 + $9 = $16.         - If my number is lower, it must be 8. Guess 8. Your total is $7 + $9 = $16.     - If my number is lower, the range is [1,6]. Guess 3.         - If this is my number, your total is $7. Otherwise, you pay $3.         - If my number is higher, the range is [4,6]. Guess 5.             - If this is my number, your total is $7 + $3 = $10. Otherwise, you pay $5.             - If my number is higher, it must be 6. Guess 6. Your total is $7 + $3 + $5 = $15.             - If my number is lower, it must be 4. Guess 4. Your total is $7 + $3 + $5 = $15.         - If my number is lower, the range is [1,2]. Guess 1.             - If this is my number, your total is $7 + $3 = $10. Otherwise, you pay $1.             - If my number is higher, it must be 2. Guess 2. Your total is $7 + $3 + $1 = $11. The worst case in all these scenarios is that you pay $16. Hence, you only need $16 to guarantee a win.
    ,
    # example 2
    [1]
    # output: 0
    # EXPLANATION:  There is only one possible number, so you can guess 1 and not have to pay anything.
    ,
    # example 3
    [2]
    # output: 1
    # EXPLANATION:  There are two possible numbers, 1 and 2. - Guess 1.     - If this is my number, your total is $0. Otherwise, you pay $1.     - If my number is higher, it must be 2. Guess 2. Your total is $1. The worst case is that you pay $1.
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
### getMoneyAmount 
import math
from math import inf
from typing import *
def f_gold(n: int) -> int:
    dp = [[0] * (n + 10) for _ in range(n + 10)]
    for l in range(2, n + 1):
        for i in range(1, n - l + 2):
            j = i + l - 1
            dp[i][j] = float('inf')
            for k in range(i, j + 1):
                t = max(dp[i][k - 1], dp[k + 1][j]) + k
                dp[i][j] = min(dp[i][j], t)
    return dp[1][n]
"-----------------"
test()

