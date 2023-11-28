
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [10, 11]
    # output: false
    # EXPLANATION:  No matter which integer the first player choose, the first player will lose. The first player can choose an integer from 1 up to 10. If the first player choose 1, the second player can only choose integers from 2 up to 10. The second player will win by choosing 10 and get a total = 11, which is >= desiredTotal. Same with other integers chosen by the first player, the second player will always win.
    ,
    # example 2
    [10, 0]
    # output: true
    ,
    # example 3
    [10, 1]
    # output: true
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
### canIWin 
def cache(f): return f
from typing import *
def f_gold(maxChoosableInteger: int, desiredTotal: int) -> bool:
    @cache
    def dfs(state, t):
        for i in range(1, maxChoosableInteger + 1):
            if (state >> i) & 1:
                continue
            if t + i >= desiredTotal or not dfs(state | 1 << i, t + i):
                return True
        return False
    s = (1 + maxChoosableInteger) * maxChoosableInteger // 2
    if s < desiredTotal:
        return False
    return dfs(0, 0)
"-----------------"
test()

