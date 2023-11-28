
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [[[7, 1, 4, 5, 6], [2, 5, 1, 6, 4], [1, 5, 4, 3, 2], [1, 2, 7, 3, 4]]]
    # output: 3
    # EXPLANATION:  The largest magic square has a size of 3. Every row sum, column sum, and diagonal sum of this magic square is equal to 12. - Row sums: 5+1+6 = 5+4+3 = 2+7+3 = 12 - Column sums: 5+5+2 = 1+4+7 = 6+3+3 = 12 - Diagonal sums: 5+4+3 = 6+4+2 = 12
    ,
    # example 2
    [[[5, 1, 3, 1], [9, 3, 3, 1], [1, 3, 3, 8]]]
    # output: 2
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
### largestMagicSquare 
from typing import *
def f_gold(grid: List[List[int]]) -> int:
    m, n = len(grid), len(grid[0])
    rowsum = [[0] * (n + 1) for _ in range(m + 1)]
    colsum = [[0] * (n + 1) for _ in range(m + 1)]
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            rowsum[i][j] = rowsum[i][j - 1] + grid[i - 1][j - 1]
            colsum[i][j] = colsum[i - 1][j] + grid[i - 1][j - 1]
    def check(x1, y1, x2, y2):
        val = rowsum[x1 + 1][y2 + 1] - rowsum[x1 + 1][y1]
        for i in range(x1 + 1, x2 + 1):
            if rowsum[i + 1][y2 + 1] - rowsum[i + 1][y1] != val:
                return False
        for j in range(y1, y2 + 1):
            if colsum[x2 + 1][j + 1] - colsum[x1][j + 1] != val:
                return False
        s, i, j = 0, x1, y1
        while i <= x2:
            s += grid[i][j]
            i += 1
            j += 1
        if s != val:
            return False
        s, i, j = 0, x1, y2
        while i <= x2:
            s += grid[i][j]
            i += 1
            j -= 1
        if s != val:
            return False
        return True
    for k in range(min(m, n), 1, -1):
        i = 0
        while i + k - 1 < m:
            j = 0
            while j + k - 1 < n:
                i2, j2 = i + k - 1, j + k - 1
                if check(i, j, i2, j2):
                    return k
                j += 1
            i += 1
    return 1
"-----------------"
test()

