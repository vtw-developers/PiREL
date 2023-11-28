
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    ["ab", "ba"]
    # output: 1
    ,
    # example 2
    ["abc", "bca"]
    # output: 2
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
### kSimilarity 
from collections import deque
from typing import *
def f_gold(s1: str, s2: str) -> int:
    def next(s):
        i = 0
        res = []
        while s[i] == s2[i]:
            i += 1
        for j in range(i + 1, n):
            if s[j] == s2[i] and s[j] != s2[j]:
                res.append(s[:i] + s[j] + s[i + 1 : j] + s[i] + s[j + 1 :])
        return res
    q = deque([s1])
    vis = {s1}
    ans, n = 0, len(s1)
    while q:
        for _ in range(len(q)):
            s = q.popleft()
            if s == s2:
                return ans
            for nxt in next(s):
                if nxt not in vis:
                    vis.add(nxt)
                    q.append(nxt)
        ans += 1
    return -1
"-----------------"
test()

