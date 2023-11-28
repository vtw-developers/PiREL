
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    ["aab"]
    # output: [["a","a","b"],["aa","b"]]
    ,
    # example 2
    ["a"]
    # output: [["a"]]
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
### partition 
from typing import *
def f_gold(s: str) -> List[List[str]]:
    ans = []
    n = len(s)
    dp = [[True] * n for _ in range(n)]
    for i in range(n - 1, -1, -1):
        for j in range(i + 1, n):
            dp[i][j] = s[i] == s[j] and dp[i + 1][j - 1]
    def dfs(s, i, t):
        nonlocal n
        if i == n:
            ans.append(t.copy())
            return
        for j in range(i, n):
            if dp[i][j]:
                t.append(s[i : j + 1])
                dfs(s, j + 1, t)
                t.pop(-1)
    dfs(s, 0, [])
    return ans
"-----------------"
test()

