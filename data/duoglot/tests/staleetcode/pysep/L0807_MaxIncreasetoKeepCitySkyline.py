### maxIncreaseKeepingSkyline 
from typing import *
def f_gold(grid: List[List[int]]) -> int:
    rmx = [max(row) for row in grid]
    cmx = [max(col) for col in zip(*grid)]
    return sum(
        (min(rmx[i], cmx[j]) - grid[i][j])
        for i in range(len(grid))
        for j in range(len(grid[0]))
    )