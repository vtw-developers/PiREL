
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [13]
    # output: 6
    ,
    # example 2
    [0]
    # output: 0
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
### countDigitOne 
from typing import *
def f_gold(n: int) -> int:
    dp = [[-1] * 10 for _ in range(10)]
    digit = []
    while n:
        digit.append(n % 10)
        n //= 10
    def dfs(pos: int, cnt: int, limit: bool) -> int:
        if pos == -1:
            return cnt
        if not limit and dp[pos][cnt] != -1:
            return dp[pos][cnt]
        up = digit[pos] if limit else 9
        ans = 0
        for i in range(up + 1):
            nxt = cnt + 1 if i == 1 else cnt
            ans += dfs(pos - 1, nxt, limit and i == digit[pos])
        if not limit:
            dp[pos][cnt] = ans
        return ans
    return dfs(len(digit) - 1, 0, True)
"-----------------"
test()

