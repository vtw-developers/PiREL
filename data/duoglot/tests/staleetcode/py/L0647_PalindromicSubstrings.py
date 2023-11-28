
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    ["abc"]
    # output: 3
    # EXPLANATION:  Three palindromic strings: "a", "b", "c".
    ,
    # example 2
    ["aaa"]
    # output: 6
    # EXPLANATION:  Six palindromic strings: "a", "a", "a", "aa", "aa", "aaa".
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
### countSubstrings 
from typing import *
def f_gold(s: str) -> int:
    t = '^#' + '#'.join(s) + '#$'
    n = len(t)
    p = [0 for _ in range(n)]
    pos, maxRight = 0, 0
    ans = 0
    for i in range(1, n - 1):
        p[i] = min(maxRight - i, p[2 * pos - i]) if maxRight > i else 1
        while t[i - p[i]] == t[i + p[i]]:
            p[i] += 1
        if i + p[i] > maxRight:
            maxRight = i + p[i]
            pos = i
        ans += p[i] // 2
    return ans
"-----------------"
test()

