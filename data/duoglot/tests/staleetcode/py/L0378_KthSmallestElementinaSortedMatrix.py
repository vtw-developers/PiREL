
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [[[1, 5, 9], [10, 11, 13], [12, 13, 15]], 8]
    # output: 13
    # EXPLANATION:  The elements in the matrix are [1,5,9,10,11,12,13,<u><strong>13</strong></u>,15], and the 8<sup>th</sup> smallest number is 13
    ,
    # example 2
    [[[-5]], 1]
    # output: -5
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
### kthSmallest 
from typing import *
def f_gold(matrix: List[List[int]], k: int) -> int:
    def check(matrix, mid, k, n):
        count = 0
        i, j = n - 1, 0
        while i >= 0 and j < n:
            if matrix[i][j] <= mid:
                count += i + 1
                j += 1
            else:
                i -= 1
        return count >= k
    n = len(matrix)
    left, right = matrix[0][0], matrix[n - 1][n - 1]
    while left < right:
        mid = (left + right) >> 1
        if check(matrix, mid, k, n):
            right = mid
        else:
            left = mid + 1
    return left
"-----------------"
test()

