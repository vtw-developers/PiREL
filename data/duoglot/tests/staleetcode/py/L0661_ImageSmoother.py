
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [[[1, 1, 1], [1, 0, 1], [1, 1, 1]]]
    # output: [[0,0,0],[0,0,0],[0,0,0]]
    # EXPLANATION:  For the points (0,0), (0,2), (2,0), (2,2): floor(3/4) = floor(0.75) = 0 For the points (0,1), (1,0), (1,2), (2,1): floor(5/6) = floor(0.83333333) = 0 For the point (1,1): floor(8/9) = floor(0.88888889) = 0
    ,
    # example 2
    [[[100, 200, 100], [200, 50, 200], [100, 200, 100]]]
    # output: [[137,141,137],[141,138,141],[137,141,137]]
    # EXPLANATION:  For the points (0,0), (0,2), (2,0), (2,2): floor((100+200+200+50)/4) = floor(137.5) = 137 For the points (0,1), (1,0), (1,2), (2,1): floor((200+200+50+200+100+100)/6) = floor(141.666667) = 141 For the point (1,1): floor((50+200+200+200+200+100+100+100+100)/9) = floor(138.888889) = 138
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
### imageSmoother 
from typing import *
def f_gold(img: List[List[int]]) -> List[List[int]]:
    m, n = len(img), len(img[0])
    ans = [[0] * n for _ in range(m)]
    for i in range(m):
        for j in range(n):
            s = cnt = 0
            for x in range(i - 1, i + 2):
                for y in range(j - 1, j + 2):
                    if 0 <= x < m and 0 <= y < n:
                        cnt += 1
                        s += img[x][y]
            ans[i][j] = s // cnt
    return ans
"-----------------"
test()

