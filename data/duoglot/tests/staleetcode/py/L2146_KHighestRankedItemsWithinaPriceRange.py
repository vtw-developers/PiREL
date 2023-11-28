
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [[[1, 2, 0, 1], [1, 3, 0, 1], [0, 2, 5, 1]], [2, 5], [0, 0], 3]
    # output: [[0,1],[1,1],[2,1]]
    # EXPLANATION:  You start at (0,0). With a price range of [2,5], we can take items from (0,1), (1,1), (2,1) and (2,2). The ranks of these items are: - (0,1) with distance 1 - (1,1) with distance 2 - (2,1) with distance 3 - (2,2) with distance 4 Thus, the 3 highest ranked items in the price range are (0,1), (1,1), and (2,1).
    ,
    # example 2
    [[[1, 2, 0, 1], [1, 3, 3, 1], [0, 2, 5, 1]], [2, 3], [2, 3], 2]
    # output: [[2,1],[1,2]]
    # EXPLANATION:  You start at (2,3). With a price range of [2,3], we can take items from (0,1), (1,1), (1,2) and (2,1). The ranks of these items are: - (2,1) with distance 2, price 2 - (1,2) with distance 2, price 3 - (1,1) with distance 3 - (0,1) with distance 4 Thus, the 2 highest ranked items in the price range are (2,1) and (1,2).
    ,
    # example 3
    [[[1, 1, 1], [0, 0, 1], [2, 3, 4]], [2, 3], [0, 0], 3]
    # output: [[2,1],[2,0]]
    # EXPLANATION:  You start at (0,0). With a price range of [2,3], we can take items from (2,0) and (2,1).  The ranks of these items are:  - (2,1) with distance 5 - (2,0) with distance 6 Thus, the 2 highest ranked items in the price range are (2,1) and (2,0).  Note that k = 3 but there are only 2 reachable items within the price range.
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
### highestRankedKItems 
from collections import deque
from typing import *
def f_gold(grid: List[List[int]], pricing: List[int], start: List[int], k: int
) -> List[List[int]]:
    m, n = len(grid), len(grid[0])
    row, col, low, high = start + pricing
    items = []
    if low <= grid[row][col] <= high:
        items.append([0, grid[row][col], row, col])
    q = deque([(row, col, 0)])
    grid[row][col] = 0
    while q:
        i, j, d = q.popleft()
        for a, b in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
            x, y = i + a, j + b
            if 0 <= x < m and 0 <= y < n and grid[x][y]:
                if low <= grid[x][y] <= high:
                    items.append([d + 1, grid[x][y], x, y])
                q.append((x, y, d + 1))
                grid[x][y] = 0
    items.sort()
    return [item[2:] for item in items][:k]
"-----------------"
test()

