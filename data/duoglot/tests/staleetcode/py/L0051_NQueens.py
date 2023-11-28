
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [4]
    # output: [[".Q..","...Q","Q...","..Q."],["..Q.","Q...","...Q",".Q.."]]
    # EXPLANATION:  There exist two distinct solutions to the 4-queens puzzle as shown above
    ,
    # example 2
    [1]
    # output: [["Q"]]
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
### solveNQueens 
from typing import *
def f_gold(n: int) -> List[List[str]]:
    res = []
    g = [['.'] * n for _ in range(n)]
    col = [False] * n
    dg = [False] * (2 * n)
    udg = [False] * (2 * n)
    def dfs(u):
        if u == n:
            res.append([''.join(item) for item in g])
            return
        for i in range(n):
            if not col[i] and not dg[u + i] and not udg[n - u + i]:
                g[u][i] = 'Q'
                col[i] = dg[u + i] = udg[n - u + i] = True
                dfs(u + 1)
                g[u][i] = '.'
                col[i] = dg[u + i] = udg[n - u + i] = False
    dfs(0)
    return res
"-----------------"
test()

