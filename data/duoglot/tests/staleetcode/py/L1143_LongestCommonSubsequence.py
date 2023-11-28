
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    ["abcde", "ace"]
    # output: 3
    # EXPLANATION:  The longest common subsequence is "ace" and its length is 3.
    ,
    # example 2
    ["abc", "abc"]
    # output: 3
    # EXPLANATION:  The longest common subsequence is "abc" and its length is 3.
    ,
    # example 3
    ["abc", "def"]
    # output: 0
    # EXPLANATION:  There is no such common subsequence, so the result is 0.
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
### longestCommonSubsequence 
from typing import *
def f_gold(text1: str, text2: str) -> int:
    m, n = len(text1), len(text2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if text1[i - 1] == text2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    return dp[-1][-1]
"-----------------"
test()

