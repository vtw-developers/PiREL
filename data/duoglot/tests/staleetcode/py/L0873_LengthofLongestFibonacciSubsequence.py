
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [[1, 2, 3, 4, 5, 6, 7, 8]]
    # output: 5
    # EXPLANATION:  The longest subsequence that is fibonacci-like: [1,2,3,5,8].
    ,
    # example 2
    [[1, 3, 7, 11, 12, 14, 18]]
    # output: 3
    # EXPLANATION: :<strong> </strong>The longest subsequence that is fibonacci-like: [1,11,12], [3,11,14] or [7,11,18].
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
### lenLongestFibSubseq 
from typing import *
def f_gold(arr: List[int]) -> int:
    mp = {v: i for i, v in enumerate(arr)}
    n = len(arr)
    dp = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(i):
            dp[j][i] = 2
    ans = 0
    for i in range(n):
        for j in range(i):
            delta = arr[i] - arr[j]
            if delta in mp:
                k = mp[delta]
                if k < j:
                    dp[j][i] = dp[k][j] + 1
                    ans = max(ans, dp[j][i])
    return ans
"-----------------"
test()

