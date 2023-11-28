
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    ["ab", "ba"]
    # output: true
    # EXPLANATION:  You can swap s[0] = 'a' and s[1] = 'b' to get "ba", which is equal to goal.
    ,
    # example 2
    ["ab", "ab"]
    # output: false
    # EXPLANATION:  The only letters you can swap are s[0] = 'a' and s[1] = 'b', which results in "ba" != goal.
    ,
    # example 3
    ["aa", "aa"]
    # output: true
    # EXPLANATION:  You can swap s[0] = 'a' and s[1] = 'a' to get "aa", which is equal to goal.
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
### buddyStrings 
from collections import Counter
from typing import *
def f_gold(s: str, goal: str) -> bool:
    m, n = len(s), len(goal)
    if m != n:
        return False
    diff = sum(1 for i in range(n) if s[i] != goal[i])
    cnt1, cnt2 = Counter(s), Counter(goal)
    if cnt1 != cnt2:
        return False
    return diff == 2 or (diff == 0 and any(e > 1 for e in cnt1.values()))
"-----------------"
test()

