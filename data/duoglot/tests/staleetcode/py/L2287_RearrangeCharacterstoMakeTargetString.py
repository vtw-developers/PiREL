
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    ["ilovecodingonleetcode", "code"]
    # output: 2
    # EXPLANATION:  For the first copy of "code", take the letters at indices 4, 5, 6, and 7. For the second copy of "code", take the letters at indices 17, 18, 19, and 20. The strings that are formed are "ecod" and "code" which can both be rearranged into "code". We can make at most two copies of "code", so we return 2.
    ,
    # example 2
    ["abcba", "abc"]
    # output: 1
    # EXPLANATION:  We can make one copy of "abc" by taking the letters at indices 0, 1, and 2. We can make at most one copy of "abc", so we return 1. Note that while there is an extra 'a' and 'b' at indices 3 and 4, we cannot reuse the letter 'c' at index 2, so we cannot make a second copy of "abc".
    ,
    # example 3
    ["abbaccaddaeea", "aaaaa"]
    # output: 1
    # EXPLANATION:  We can make one copy of "aaaaa" by taking the letters at indices 0, 3, 6, 9, and 12. We can make at most one copy of "aaaaa", so we return 1.
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
### rearrangeCharacters 
import math
from math import inf
from collections import Counter
from typing import *
def f_gold(s: str, target: str) -> int:
    cnt = Counter(s)
    cnt2 = Counter(target)
    ans = float('inf')
    for c, v in cnt2.items():
        if cnt[c] < v:
            return 0
        ans = min(ans, cnt[c] // v)
    return ans
"-----------------"
test()

