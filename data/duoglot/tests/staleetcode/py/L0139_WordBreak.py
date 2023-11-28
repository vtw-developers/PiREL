
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    ["leetcode", ["leet", "code"]]
    # output: true
    # EXPLANATION:  Return true because "leetcode" can be segmented as "leet code".
    ,
    # example 2
    ["applepenapple", ["apple", "pen"]]
    # output: true
    # EXPLANATION:  Return true because "applepenapple" can be segmented as "apple pen apple". Note that you are allowed to reuse a dictionary word.
    ,
    # example 3
    ["catsandog", ["cats", "dog", "sand", "and", "cat"]]
    # output: false
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
### wordBreak 
from typing import *
def f_gold(s: str, wordDict: List[str]) -> bool:
    words = set(wordDict)
    n = len(s)
    dp = [False] * (n + 1)
    dp[0] = True
    for i in range(1, n + 1):
        for j in range(i):
            if dp[j] and s[j:i] in words:
                dp[i] = True
                break
    return dp[n]
"-----------------"
test()

