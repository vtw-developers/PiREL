
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [[1, 5, 5, 4, 11], [[0, 1], [1, 2], [1, 3], [3, 4]]]
    # output: 9
    # EXPLANATION:  The diagram above shows a way to make a pair of removals. - The 1<sup>st</sup> component has nodes [1,3,4] with values [5,4,11]. Its XOR value is 5 ^ 4 ^ 11 = 10. - The 2<sup>nd</sup> component has node [0] with value [1]. Its XOR value is 1 = 1. - The 3<sup>rd</sup> component has node [2] with value [5]. Its XOR value is 5 = 5. The score is the difference between the largest and smallest XOR value which is 10 - 1 = 9. It can be shown that no other pair of removals will obtain a smaller score than 9.
    ,
    # example 2
    [[5, 5, 2, 4, 4, 2], [[0, 1], [1, 2], [5, 2], [4, 3], [1, 3]]]
    # output: 0
    # EXPLANATION:  The diagram above shows a way to make a pair of removals. - The 1<sup>st</sup> component has nodes [3,4] with values [4,4]. Its XOR value is 4 ^ 4 = 0. - The 2<sup>nd</sup> component has nodes [1,0] with values [5,5]. Its XOR value is 5 ^ 5 = 0. - The 3<sup>rd</sup> component has nodes [2,5] with values [2,2]. Its XOR value is 2 ^ 2 = 0. The score is the difference between the largest and smallest XOR value which is 0 - 0 = 0. We cannot obtain a smaller score than 0.
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
### minimumScore 
import math
from math import inf
from collections import defaultdict
from typing import *
def f_gold(nums: List[int], edges: List[List[int]]) -> int:
    def dfs(i, fa, x):
        res = nums[i]
        for j in g[i]:
            if j != fa and j != x:
                res ^= dfs(j, i, x)
        return res
    def dfs2(i, fa, x):
        nonlocal s, s1, ans
        res = nums[i]
        for j in g[i]:
            if j != fa and j != x:
                a = dfs2(j, i, x)
                res ^= a
                b = s1 ^ a
                c = s ^ s1
                t = max(a, b, c) - min(a, b, c)
                ans = min(ans, t)
        return res
    g = defaultdict(list)
    for a, b in edges:
        g[a].append(b)
        g[b].append(a)
    s = 0
    for v in nums:
        s ^= v
    n = len(nums)
    ans = inf
    for i in range(n):
        for j in g[i]:
            s1 = dfs(i, -1, j)
            dfs2(i, -1, j)
    return ans
"-----------------"
test()

