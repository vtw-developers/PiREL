### subsetsWithDup 
from typing import *
def f_gold(nums: List[int]) -> List[List[int]]:
    def dfs(u, t):
        ans.append(t[:])
        for i in range(u, len(nums)):
            if i != u and nums[i] == nums[i - 1]:
                continue
            t.append(nums[i])
            dfs(i + 1, t)
            t.pop()
    ans = []
    nums.sort()
    dfs(0, [])
    return ans