### searchMatrix 
from typing import *
def f_gold(matrix: List[List[int]], target: int) -> bool:
    m, n = len(matrix), len(matrix[0])
    left, right = 0, m * n - 1
    while left < right:
        mid = (left + right) >> 1
        x, y = divmod(mid, n)
        if matrix[x][y] >= target:
            right = mid
        else:
            left = mid + 1
    return matrix[left // n][left % n] == target