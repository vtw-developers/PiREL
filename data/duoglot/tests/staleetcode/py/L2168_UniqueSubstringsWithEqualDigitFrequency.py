
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    ["1212"]
    # output: 5
    # EXPLANATION:  The substrings that meet the requirements are "1", "2", "12", "21", "1212". Note that although the substring "12" appears twice, it is only counted once.
    ,
    # example 2
    ["12321"]
    # output: 9
    # EXPLANATION:  The substrings that meet the requirements are "1", "2", "3", "12", "23", "32", "21", "123", "321".
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
### equalDigitFrequency 
from typing import *
def f_gold(s: str) -> int:
    def check(i, j):
        v = set()
        for k in range(10):
            cnt = presum[j + 1][k] - presum[i][k]
            if cnt > 0:
                v.add(cnt)
            if len(v) > 1:
                return False
        return True
    n = len(s)
    presum = [[0] * 10 for _ in range(n + 1)]
    for i, c in enumerate(s):
        presum[i + 1][int(c)] += 1
        for j in range(10):
            presum[i + 1][j] += presum[i][j]
    vis = set(s[i : j + 1] for i in range(n) for j in range(i, n) if check(i, j))
    return len(vis)
"-----------------"
test()

