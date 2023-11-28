
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    ["aa", "a"]
    # output: false
    # EXPLANATION:  "a" does not match the entire string "aa".
    ,
    # example 2
    ["aa", "a*"]
    # output: true
    # EXPLANATION:  '*' means zero or more of the preceding element, 'a'. Therefore, by repeating 'a' once, it becomes "aa".
    ,
    # example 3
    ["ab", ".*"]
    # output: true
    # EXPLANATION:  ".*" means "zero or more (*) of any character (.)".
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
### isMatch 
from typing import *
def f_gold(s: str, p: str) -> bool:
    m, n = len(s), len(p)
    if n == 0:
        return m == 0
    dp = [[False] * (n + 1) for _ in range(m + 1)]
    dp[0][0] = True
    for j in range(2, n + 1):
        if p[j - 1] == '*':
            dp[0][j] = dp[0][j - 2]
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if s[i - 1] == p[j - 1] or p[j - 1] == '.':
                dp[i][j] = dp[i - 1][j - 1]
            elif p[j - 1] == '*':
                if p[j - 2] == '.' or p[j - 2] == s[i - 1]:
                    dp[i][j] = dp[i][j - 2] or dp[i - 1][j]
                else:
                    dp[i][j] = dp[i][j - 2]
    return dp[-1][-1]
"-----------------"
test()

