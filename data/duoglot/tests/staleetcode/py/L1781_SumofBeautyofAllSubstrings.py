
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    ["aabcb"]
    # output: 5
    # EXPLANATION: The substrings with non-zero beauty are ["aab","aabc","aabcb","abcb","bcb"], each with beauty equal to 1.
    ,
    # example 2
    ["aabcbaa"]
    # output: 17
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
### beautySum 
from collections import Counter
from typing import *
def f_gold(s: str) -> int:
    ans, n = 0, len(s)
    for i in range(n):
        counter = Counter()
        for j in range(i, n):
            counter[s[j]] += 1
            t = [v for v in counter.values() if v]
            ans += max(t) - min(t)
    return ans
"-----------------"
test()

