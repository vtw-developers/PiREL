
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    ["123"]
    # output: "121"
    ,
    # example 2
    ["1"]
    # output: "0"
    # EXPLANATION:  0 and 2 are the closest palindromes but we return the smallest which is 0.
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
### nearestPalindromic 
from typing import *
def f_gold(n: str) -> str:
    x = int(n)
    l = len(n)
    res = {10 ** (l - 1) - 1, 10**l + 1}
    left = int(n[: (l + 1) >> 1])
    for i in range(left - 1, left + 2):
        j = i if l % 2 == 0 else i // 10
        while j:
            i = i * 10 + j % 10
            j //= 10
        res.add(i)
    res.discard(x)
    ans = -1
    for t in res:
        if (
            ans == -1
            or abs(t - x) < abs(ans - x)
            or (abs(t - x) == abs(ans - x) and t < ans)
        ):
            ans = t
    return str(ans)
"-----------------"
test()

