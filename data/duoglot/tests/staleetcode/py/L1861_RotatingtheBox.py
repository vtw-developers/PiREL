
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [[["#", ".", "#"]]]
    # output: [["."],         ["#"],         ["#"]]
    ,
    # example 2
    [[["#", ".", "*", "."], ["#", "#", "*", "."]]]
    # output: [["#","."],         ["#","#"],         ["*","*"],         [".","."]]
    ,
    # example 3
    [[["#", "#", "*", ".", "*", "."], ["#", "#", "#", "*", ".", "."], ["#", "#", "#", ".", "#", "."]]]
    # output: [[".","#","#"],         [".","#","#"],         ["#","#","*"],         ["#","*","."],         ["#",".","*"],         ["#",".","."]]
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
### rotateTheBox 
from collections import deque
from typing import *
def f_gold(box: List[List[str]]) -> List[List[str]]:
    m, n = len(box), len(box[0])
    res = [[None] * m for _ in range(n)]
    for i in range(m):
        for j in range(n):
            res[j][m - i - 1] = box[i][j]
    for j in range(m):
        q = deque()
        for i in range(n - 1, -1, -1):
            if res[i][j] == '*':
                q.clear()
                continue
            if res[i][j] == '.':
                q.append(i)
            else:
                if not q:
                    continue
                res[q.popleft()][j] = '#'
                res[i][j] = '.'
                q.append(i)
    return res
"-----------------"
test()

