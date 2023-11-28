
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [[[1, 0, 0], [0, 1, 1], [0, 1, 1]]]
    # output: [[0,0,0,0],[1,1,2,2]]
    # EXPLANATION:  The first group has a top left corner at land[0][0] and a bottom right corner at land[0][0]. The second group has a top left corner at land[1][1] and a bottom right corner at land[2][2].
    ,
    # example 2
    [[[1, 1], [1, 1]]]
    # output: [[0,0,1,1]]
    # EXPLANATION:  The first group has a top left corner at land[0][0] and a bottom right corner at land[1][1].
    ,
    # example 3
    [[[0]]]
    # output: []
    # EXPLANATION:  There are no groups of farmland.
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
### findFarmland 
from typing import *
def f_gold(land: List[List[int]]) -> List[List[int]]:
    m, n = len(land), len(land[0])
    ans = []
    for i in range(m):
        for j in range(n):
            if (
                land[i][j] == 0
                or (j > 0 and land[i][j - 1] == 1)
                or (i > 0 and land[i - 1][j] == 1)
            ):
                continue
            x, y = i, j
            while x + 1 < m and land[x + 1][j] == 1:
                x += 1
            while y + 1 < n and land[x][y + 1] == 1:
                y += 1
            ans.append([i, j, x, y])
    return ans
"-----------------"
test()

