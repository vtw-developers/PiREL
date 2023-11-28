
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [[3, 9, 7, 3]]
    # output: 2
    # EXPLANATION:  One optimal partition is: [3,9] and [7,3]. The absolute difference between the sums of the arrays is abs((3 + 9) - (7 + 3)) = 2.
    ,
    # example 2
    [[-36, 36]]
    # output: 72
    # EXPLANATION:  One optimal partition is: [-36] and [36]. The absolute difference between the sums of the arrays is abs((-36) - (36)) = 72.
    ,
    # example 3
    [[2, -1, 0, 4, -2, -9]]
    # output: 0
    # EXPLANATION:  One optimal partition is: [2,4,-9] and [-1,0,-2]. The absolute difference between the sums of the arrays is abs((2 + 4 + -9) - (-1 + 0 + -2)) = 0.
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
### minimumDifference 
import math
from math import inf
from collections import defaultdict
from typing import *
def f_gold(nums: List[int]) -> int:
    n = len(nums) >> 1
    f = defaultdict(set)
    g = defaultdict(set)
    for i in range(1 << n):
        s = cnt = 0
        s1 = cnt1 = 0
        for j in range(n):
            if (i & (1 << j)) != 0:
                s += nums[j]
                cnt += 1
                s1 += nums[n + j]
                cnt1 += 1
            else:
                s -= nums[j]
                s1 -= nums[n + j]
        f[cnt].add(s)
        g[cnt1].add(s1)
    ans = float('inf')
    for i in range(n + 1):
        fi, gi = sorted(list(f[i])), sorted(list(g[n - i]))
        # min(abs(f[i] + g[n - i]))
        for a in fi:
            left, right = 0, len(gi) - 1
            b = -a
            while left < right:
                mid = (left + right) >> 1
                if gi[mid] >= b:
                    right = mid
                else:
                    left = mid + 1
            ans = min(ans, abs(a + gi[left]))
            if left > 0:
                ans = min(ans, abs(a + gi[left - 1]))
    return ans
"-----------------"
test()

