
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    ["great", "rgeat"]
    # output: true
    # EXPLANATION:  One possible scenario applied on s1 is: "great" --> "gr/eat" // divide at random index. "gr/eat" --> "gr/eat" // random decision is not to swap the two substrings and keep them in order. "gr/eat" --> "g/r / e/at" // apply the same algorithm recursively on both substrings. divide at random index each of them. "g/r / e/at" --> "r/g / e/at" // random decision was to swap the first substring and to keep the second substring in the same order. "r/g / e/at" --> "r/g / e/ a/t" // again apply the algorithm recursively, divide "at" to "a/t". "r/g / e/ a/t" --> "r/g / e/ a/t" // random decision is to keep both substrings in the same order. The algorithm stops now, and the result string is "rgeat" which is s2. As one possible scenario led s1 to be scrambled to s2, we return true.
    ,
    # example 2
    ["abcde", "caebd"]
    # output: false
    ,
    # example 3
    ["a", "a"]
    # output: true
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
### isScramble 
from typing import *
def f_gold(s1: str, s2: str) -> bool:
    n = len(s1)
    dp = [[[False] * (n + 1) for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            dp[i][j][1] = s1[i] == s2[j]
    for l in range(2, n + 1):
        for i1 in range(n - l + 1):
            for i2 in range(n - l + 1):
                for i in range(1, l):
                    if dp[i1][i2][i] and dp[i1 + i][i2 + i][l - i]:
                        dp[i1][i2][l] = True
                        break
                    if dp[i1][i2 + l - i][i] and dp[i1 + i][i2][l - i]:
                        dp[i1][i2][l] = True
                        break
    return dp[0][0][n]
"-----------------"
test()

