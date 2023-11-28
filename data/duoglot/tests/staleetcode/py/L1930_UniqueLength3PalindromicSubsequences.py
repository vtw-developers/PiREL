
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    ["aabca"]
    # output: 3
    # EXPLANATION:  The 3 palindromic subsequences of length 3 are: - "aba" (subsequence of "<u>a</u>a<u>b</u>c<u>a</u>") - "aaa" (subsequence of "<u>aa</u>bc<u>a</u>") - "aca" (subsequence of "<u>a</u>ab<u>ca</u>")
    ,
    # example 2
    ["adc"]
    # output: 0
    # EXPLANATION:  There are no palindromic subsequences of length 3 in "adc".
    ,
    # example 3
    ["bbcbaba"]
    # output: 4
    # EXPLANATION:  The 4 palindromic subsequences of length 3 are: - "bbb" (subsequence of "<u>bb</u>c<u>b</u>aba") - "bcb" (subsequence of "<u>b</u>b<u>cb</u>aba") - "bab" (subsequence of "<u>b</u>bcb<u>ab</u>a") - "aba" (subsequence of "bbcb<u>aba</u>")
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
### countPalindromicSubsequence 
from typing import *
def f_gold(s: str) -> int:
    res = 0
    for i in range(26):
        c = chr(ord('a') + i)
        if c in s:
            l, r = s.index(c), s.rindex(c)
            chars = {s[j] for j in range(l + 1, r)}
            res += len(chars)
    return res
"-----------------"
test()

