
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [["10", "0001", "111001", "1", "0"], 5, 3]
    # output: 4
    # EXPLANATION:  The largest subset with at most 5 0's and 3 1's is {"10", "0001", "1", "0"}, so the answer is 4. Other valid but smaller subsets include {"0001", "1"} and {"10", "1", "0"}. {"111001"} is an invalid subset because it contains 4 1's, greater than the maximum of 3.
    ,
    # example 2
    [["10", "0", "1"], 1, 1]
    # output: 2
    # EXPLANATION:  The largest subset is {"0", "1"}, so the answer is 2.
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
### findMaxForm 
from typing import *
def f_gold(strs: List[str], m: int, n: int) -> int:
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    t = [(s.count('0'), s.count('1')) for s in strs]
    for k in range(len(strs)):
        n0, n1 = t[k]
        for i in range(m, n0 - 1, -1):
            for j in range(n, n1 - 1, -1):
                dp[i][j] = max(dp[i][j], dp[i - n0][j - n1] + 1)
    return dp[-1][-1]
"-----------------"
test()

