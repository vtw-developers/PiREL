
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    ["fool3e7bar", "leet", [["e", "3"], ["t", "7"], ["t", "8"]]]
    # output: true
    # EXPLANATION:  Replace the first 'e' in sub with '3' and 't' in sub with '7'. Now sub = "l3e7" is a substring of s, so we return true.
    ,
    # example 2
    ["fooleetbar", "f00l", [["o", "0"]]]
    # output: false
    # EXPLANATION:  The string "f00l" is not a substring of s and no replacements can be made. Note that we cannot replace '0' with 'o'.
    ,
    # example 3
    ["Fool33tbaR", "leetd", [["e", "3"], ["t", "7"], ["t", "8"], ["d", "b"], ["p", "b"]]]
    # output: true
    # EXPLANATION:  Replace the first and second 'e' in sub with '3' and 'd' in sub with 'b'. Now sub = "l33tb" is a substring of s, so we return true.
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
### matchReplacement 
from collections import defaultdict
from typing import *
def f_gold(s: str, sub: str, mappings: List[List[str]]) -> bool:
    d = defaultdict(set)
    for a, b in mappings:
        d[a].add(b)
    n, k = len(s), len(sub)
    for i in range(n - k + 1):
        flag = True
        for j in range(k):
            a, b = s[i + j], sub[j]
            if a == b or a in d[b]:
                continue
            else:
                flag = False
                break
        if flag:
            return True
    return False
"-----------------"
test()

