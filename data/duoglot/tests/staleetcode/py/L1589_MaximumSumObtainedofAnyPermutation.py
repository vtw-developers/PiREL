
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [[1, 2, 3, 4, 5], [[1, 3], [0, 1]]]
    # output: 19
    # EXPLANATION:  One permutation of nums is [2,1,3,4,5] with the following result:  requests[0] -> nums[1] + nums[2] + nums[3] = 1 + 3 + 4 = 8 requests[1] -> nums[0] + nums[1] = 2 + 1 = 3 Total sum: 8 + 3 = 11. A permutation with a higher total sum is [3,5,4,2,1] with the following result: requests[0] -> nums[1] + nums[2] + nums[3] = 5 + 4 + 2 = 11 requests[1] -> nums[0] + nums[1] = 3 + 5  = 8 Total sum: 11 + 8 = 19, which is the best that you can do.
    ,
    # example 2
    [[1, 2, 3, 4, 5, 6], [[0, 1]]]
    # output: 11
    # EXPLANATION:  A permutation with the max total sum is [6,5,4,3,2,1] with request sums [11].
    ,
    # example 3
    [[1, 2, 3, 4, 5, 10], [[0, 2], [1, 3], [1, 1]]]
    # output: 47
    # EXPLANATION:  A permutation with the max total sum is [4,10,5,3,2,1] with request sums [19,18,10].
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
### maxSumRangeQuery 
from typing import *
def f_gold(nums: List[int], requests: List[List[int]]) -> int:
    n = 100010
    delta = [0] * n
    for start, end in requests:
        delta[start] += 1
        delta[end + 1] -= 1
    for i in range(1, n):
        delta[i] += delta[i - 1]
    nums.sort()
    delta.sort()
    i, j, res = n - 1, len(nums) - 1, 0
    while i > 0 and delta[i] > 0:
        res += delta[i] * nums[j]
        i -= 1
        j -= 1
    return res % 1000000007
"-----------------"
test()

