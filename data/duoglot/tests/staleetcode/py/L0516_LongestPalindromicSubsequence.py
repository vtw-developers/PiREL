
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    ["bbbab"]
    # output: 4
    # EXPLANATION:  One possible longest palindromic subsequence is "bbbb".
    ,
    # example 2
    ["cbbd"]
    # output: 2
    # EXPLANATION:  One possible longest palindromic subsequence is "bb".
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
### longestPalindromeSubseq 
from typing import *
def f_gold(s: str) -> int:
    n = len(s)
    dp = [[0] * n for _ in range(n)]
    for i in range(n):
        dp[i][i] = 1
    for j in range(1, n):
        for i in range(j - 1, -1, -1):
            if s[i] == s[j]:
                dp[i][j] = dp[i + 1][j - 1] + 2
            else:
                dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])
    return dp[0][-1]
"-----------------"
test()

