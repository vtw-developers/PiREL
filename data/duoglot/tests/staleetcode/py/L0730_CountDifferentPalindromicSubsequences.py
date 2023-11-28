
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    ["bccb"]
    # output: 6
    # EXPLANATION:  The 6 different non-empty palindromic subsequences are 'b', 'c', 'bb', 'cc', 'bcb', 'bccb'. Note that 'bcb' is counted only once, even though it occurs twice.
    ,
    # example 2
    ["abcdabcdabcdabcdabcdabcdabcdabcddcbadcbadcbadcbadcbadcbadcbadcba"]
    # output: 104860361
    # EXPLANATION:  There are 3104860382 different non-empty palindromic subsequences, which is 104860361 modulo 10<sup>9</sup> + 7.
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
### countPalindromicSubsequences 
from typing import *
def f_gold(s: str) -> int:
    mod = 10**9 + 7
    n = len(s)
    dp = [[[0] * 4 for _ in range(n)] for _ in range(n)]
    for i, c in enumerate(s):
        dp[i][i][ord(c) - ord('a')] = 1
    for l in range(2, n + 1):
        for i in range(n - l + 1):
            j = i + l - 1
            for c in 'abcd':
                k = ord(c) - ord('a')
                if s[i] == s[j] == c:
                    dp[i][j][k] = 2 + sum(dp[i + 1][j - 1])
                elif s[i] == c:
                    dp[i][j][k] = dp[i][j - 1][k]
                elif s[j] == c:
                    dp[i][j][k] = dp[i + 1][j][k]
                else:
                    dp[i][j][k] = dp[i + 1][j - 1][k]
    return sum(dp[0][-1]) % mod
"-----------------"
test()

