
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    ["abcabcabc"]
    # output: 3
    # EXPLANATION: The 3 substrings are "abcabc", "bcabca" and "cabcab".
    ,
    # example 2
    ["leetcodeleetcode"]
    # output: 2
    # EXPLANATION: The 2 substrings are "ee" and "leetcodeleetcode".
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
### distinctEchoSubstrings 
from typing import *
def f_gold(text: str) -> int:
    def get(l, r):
        return (h[r] - h[l - 1] * p[r - l + 1]) % mod
    n = len(text)
    base = 131
    mod = int(1e9) + 7
    h = [0] * (n + 10)
    p = [1] * (n + 10)
    for i, c in enumerate(text):
        t = ord(c) - ord('a') + 1
        h[i + 1] = (h[i] * base) % mod + t
        p[i + 1] = (p[i] * base) % mod
    vis = set()
    for i in range(n - 1):
        for j in range(i + 1, n, 2):
            k = (i + j) >> 1
            a = get(i + 1, k + 1)
            b = get(k + 2, j + 1)
            if a == b:
                vis.add(a)
    return len(vis)
"-----------------"
test()

