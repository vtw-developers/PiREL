
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    ["aab"]
    # output: 1
    # EXPLANATION:  The palindrome partitioning ["aa","b"] could be produced using 1 cut.
    ,
    # example 2
    ["a"]
    # output: 0
    ,
    # example 3
    ["ab"]
    # output: 1
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
### minCut 
from typing import *
def f_gold(s: str) -> int:
    n = len(s)
    dp1 = [[False] * n for _ in range(n)]
    for i in range(n - 1, -1, -1):
        for j in range(i, n):
            dp1[i][j] = s[i] == s[j] and (j - 1 < 3 or dp1[i + 1][j - 1])
    dp2 = [0] * n
    for i in range(n):
        if not dp1[0][i]:
            dp2[i] = i
            for j in range(1, i + 1):
                if dp1[j][i]:
                    dp2[i] = min(dp2[i], dp2[j - 1] + 1)
    return dp2[-1]
"-----------------"
test()

