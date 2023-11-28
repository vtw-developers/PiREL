
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [["a", "b", "ba", "bca", "bda", "bdca"]]
    # output: 4
    # EXPLANATION: : One of the longest word chains is ["a","<u>b</u>a","b<u>d</u>a","bd<u>c</u>a"].
    ,
    # example 2
    [["xbc", "pcxbcf", "xb", "cxbc", "pcxbc"]]
    # output: 5
    # EXPLANATION:  All the words can be put in a word chain ["xb", "xb<u>c</u>", "<u>c</u>xbc", "<u>p</u>cxbc", "pcxbc<u>f</u>"].
    ,
    # example 3
    [["abcd", "dbqca"]]
    # output: 1
    # EXPLANATION:  The trivial word chain ["abcd"] is one of the longest word chains. ["abcd","dbqca"] is not a valid word chain because the ordering of the letters is changed.
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
### longestStrChain 
from typing import *
def f_gold(words: List[str]) -> int:
    def check(w1, w2):
        if len(w2) - len(w1) != 1:
            return False
        i = j = cnt = 0
        while i < len(w1) and j < len(w2):
            if w1[i] != w2[j]:
                cnt += 1
            else:
                i += 1
            j += 1
        return cnt < 2 and i == len(w1)
    n = len(words)
    dp = [1] * (n + 1)
    words.sort(key=lambda x: len(x))
    res = 1
    for i in range(1, n):
        for j in range(i):
            if check(words[j], words[i]):
                dp[i] = max(dp[i], dp[j] + 1)
        res = max(res, dp[i])
    return res
"-----------------"
test()

