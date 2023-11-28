
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    ["babad"]
    # output: "bab"
    # EXPLANATION:  "aba" is also a valid answer.
    ,
    # example 2
    ["cbbd"]
    # output: "bb"
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
### longestPalindrome 
from typing import *
def f_gold(s: str) -> str:
    n = len(s)
    dp = [[False] * n for _ in range(n)]
    start, mx = 0, 1
    for j in range(n):
        for i in range(j + 1):
            if j - i < 2:
                dp[i][j] = s[i] == s[j]
            else:
                dp[i][j] = dp[i + 1][j - 1] and s[i] == s[j]
            if dp[i][j] and mx < j - i + 1:
                start, mx = i, j - i + 1
    return s[start : start + mx]
"-----------------"
test()

