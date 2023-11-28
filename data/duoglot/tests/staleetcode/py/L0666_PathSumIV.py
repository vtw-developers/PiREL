
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [[113, 215, 221]]
    # output: 12
    # EXPLANATION:  The tree that the list represents is shown. The path sum is (3 + 5) + (3 + 1) = 12.
    ,
    # example 2
    [[113, 221]]
    # output: 4
    # EXPLANATION:  The tree that the list represents is shown.  The path sum is (3 + 1) = 4.
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
### pathSum 
from typing import *
def f_gold(nums: List[int]) -> int:
    def dfs(node, t):
        if node not in mp:
            return
        t += mp[node]
        d, p = divmod(node, 10)
        l = (d + 1) * 10 + (p * 2) - 1
        r = l + 1
        nonlocal ans
        if l not in mp and r not in mp:
            ans += t
            return
        dfs(l, t)
        dfs(r, t)
    ans = 0
    mp = {num // 10: num % 10 for num in nums}
    dfs(11, 0)
    return ans
"-----------------"
test()

