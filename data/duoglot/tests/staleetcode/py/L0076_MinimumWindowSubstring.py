
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    ["ADOBECODEBANC", "ABC"]
    # output: "BANC"
    # EXPLANATION:  The minimum window substring "BANC" includes 'A', 'B', and 'C' from string t.
    ,
    # example 2
    ["a", "a"]
    # output: "a"
    # EXPLANATION:  The entire string s is the minimum window.
    ,
    # example 3
    ["a", "aa"]
    # output: ""
    # EXPLANATION:  Both 'a's from t must be included in the window. Since the largest window of s only has one 'a', return empty string.
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
### minWindow 
import math
from math import inf
from collections import Counter
from typing import *
def f_gold(s: str, t: str) -> str:
    ans = ''
    m, n = len(s), len(t)
    if m < n:
        return ans
    need = Counter(t)
    window = Counter()
    i, cnt, mi = 0, 0, float('inf')
    for j, c in enumerate(s):
        window[c] += 1
        if need[c] >= window[c]:
            cnt += 1
        while cnt == n:
            if j - i + 1 < mi:
                mi = j - i + 1
                ans = s[i : j + 1]
            c = s[i]
            if need[c] >= window[c]:
                cnt -= 1
            window[c] -= 1
            i += 1
    return ans
"-----------------"
test()

