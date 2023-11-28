### minDifference 
import math
from math import inf
from typing import *
def f_gold(nums: List[int], queries: List[List[int]]) -> List[int]:
    m, n = len(nums), len(queries)
    pre_sum = [[0] * 101 for _ in range(m + 1)]
    for i in range(1, m + 1):
        for j in range(1, 101):
            t = 1 if nums[i - 1] == j else 0
            pre_sum[i][j] = pre_sum[i - 1][j] + t
    ans = []
    for i in range(n):
        left, right = queries[i][0], queries[i][1] + 1
        t = float('inf')
        last = -1
        for j in range(1, 101):
            if pre_sum[right][j] - pre_sum[left][j] > 0:
                if last != -1:
                    t = min(t, j - last)
                last = j
        if t == float('inf'):
            t = -1
        ans.append(t)
    return ans