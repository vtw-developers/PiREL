
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [[4, 3, 2, 3, 5, 2, 1], 4]
    # output: true
    # EXPLANATION:  It is possible to divide it into 4 subsets (5), (1, 4), (2,3), (2,3) with equal sums.
    ,
    # example 2
    [[1, 2, 3, 4], 3]
    # output: false
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
### canPartitionKSubsets 
from typing import *
def f_gold(nums: List[int], k: int) -> bool:
    s = sum(nums)
    target, m = divmod(s, k)
    if m != 0:
        return False
    cur = [0] * k
    n = len(nums)
    def dfs(i: int) -> bool:
        if i == n:
            return True
        for j in range(k):
            if j > 0 and cur[j - 1] == cur[j]:
                continue
            cur[j] += nums[i]
            if cur[j] <= target and dfs(i + 1):
                return True
            cur[j] -= nums[i]
        return False
    nums.sort(reverse=True)
    return dfs(0)
"-----------------"
test()

