
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [["babca", "bbazb"]]
    # output: 3
    # EXPLANATION:  After deleting columns 0, 1, and 4, the final array is strs = ["bc", "az"]. Both these rows are individually in lexicographic order (ie. strs[0][0] <= strs[0][1] and strs[1][0] <= strs[1][1]). Note that strs[0] > strs[1] - the array strs is not necessarily in lexicographic order.
    ,
    # example 2
    [["edcba"]]
    # output: 4
    # EXPLANATION:  If we delete less than 4 columns, the only row will not be lexicographically sorted.
    ,
    # example 3
    [["ghi", "def", "abc"]]
    # output: 0
    # EXPLANATION:  All rows are already lexicographically sorted.
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
### minDeletionSize 
from typing import *
def f_gold(strs: List[str]) -> int:
    n = len(strs[0])
    dp = [1] * n
    for i in range(1, n):
        for j in range(i):
            if all(s[j] <= s[i] for s in strs):
                dp[i] = max(dp[i], dp[j] + 1)
    return n - max(dp)
"-----------------"
test()

