### subsets 
from typing import *
def f_gold(nums: List[int]) -> List[List[int]]:
    def dfs(u, t):
        if u == len(nums):
            ans.append(t[:])
            return
        dfs(u + 1, t)
        t.append(nums[u])
        dfs(u + 1, t)
        t.pop()
    ans = []
    dfs(0, [])
    return ans