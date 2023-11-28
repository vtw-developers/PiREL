
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [[1, 3, 4, 8], [[0, 1], [1, 2], [2, 3], [0, 3]]]
    # output: [2,1,4,1]
    # EXPLANATION:  The queries are processed as follows: - queries[0] = [0,1]: The subarray is [<u>1</u>,<u>3</u>] and the minimum absolute difference is |1-3| = 2. - queries[1] = [1,2]: The subarray is [<u>3</u>,<u>4</u>] and the minimum absolute difference is |3-4| = 1. - queries[2] = [2,3]: The subarray is [<u>4</u>,<u>8</u>] and the minimum absolute difference is |4-8| = 4. - queries[3] = [0,3]: The subarray is [1,<u>3</u>,<u>4</u>,8] and the minimum absolute difference is |3-4| = 1.
    ,
    # example 2
    [[4, 5, 2, 2, 7, 10], [[2, 3], [0, 2], [0, 5], [3, 5]]]
    # output: [-1,1,1,3]
    # EXPLANATION: The queries are processed as follows: - queries[0] = [2,3]: The subarray is [2,2] and the minimum absolute difference is -1 because all the   elements are the same. - queries[1] = [0,2]: The subarray is [<u>4</u>,<u>5</u>,2] and the minimum absolute difference is |4-5| = 1. - queries[2] = [0,5]: The subarray is [<u>4</u>,<u>5</u>,2,2,7,10] and the minimum absolute difference is |4-5| = 1. - queries[3] = [3,5]: The subarray is [2,<u>7</u>,<u>10</u>] and the minimum absolute difference is |7-10| = 3.
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
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
"-----------------"
test()

