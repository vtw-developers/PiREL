
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [[[3, 4], [4, 5], [5]]]
    # output: 1
    # EXPLANATION:  There is only one way to choose hats given the conditions.  First person choose hat 3, Second person choose hat 4 and last one hat 5.
    ,
    # example 2
    [[[3, 5, 1], [3, 5]]]
    # output: 4
    # EXPLANATION:  There are 4 ways to choose hats: (3,5), (5,3), (1,3) and (1,5)
    ,
    # example 3
    [[[1, 2, 3, 4], [1, 2, 3, 4], [1, 2, 3, 4], [1, 2, 3, 4]]]
    # output: 24
    # EXPLANATION:  Each person can choose hats labeled from 1 to 4. Number of Permutations of (1,2,3,4) = 24.
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
### numberWays 
from collections import defaultdict
from typing import *
def f_gold(hats: List[List[int]]) -> int:
    d = defaultdict(list)
    for i, h in enumerate(hats):
        for v in h:
            d[v].append(i)
    n = len(hats)
    mx = max(max(h) for h in hats)
    dp = [[0] * (1 << n) for _ in range(mx + 1)]
    dp[0][0] = 1
    mod = int(1e9) + 7
    for i in range(1, mx + 1):
        for mask in range(1 << n):
            dp[i][mask] = dp[i - 1][mask]
            for j in d[i]:
                if (mask >> j) & 1:
                    dp[i][mask] += dp[i - 1][mask ^ (1 << j)]
            dp[i][mask] %= mod
    return dp[mx][(1 << n) - 1]
"-----------------"
test()

