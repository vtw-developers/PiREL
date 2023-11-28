
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    ["aabcc", "dbbca", "aadbbcbcac"]
    # output: true
    ,
    # example 2
    ["aabcc", "dbbca", "aadbbbaccc"]
    # output: false
    ,
    # example 3
    ["", "", ""]
    # output: true
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
### isInterleave 
def cache(f): return f
from typing import *
def f_gold(s1: str, s2: str, s3: str) -> bool:
    m, n = len(s1), len(s2)
    if m + n != len(s3):
        return False
    @cache
    def dfs(i, j):
        if i == m and j == n:
            return True
        return (
            i < m
            and s1[i] == s3[i + j]
            and dfs(i + 1, j)
            or j < n
            and s2[j] == s3[i + j]
            and dfs(i, j + 1)
        )
    return dfs(0, 0)
"-----------------"
test()

