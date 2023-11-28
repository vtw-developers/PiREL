
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [[["(", "(", "("], [")", "(", ")"], ["(", "(", ")"], ["(", "(", ")"]]]
    # output: true
    # EXPLANATION:  The above diagram shows two possible paths that form valid parentheses strings. The first path shown results in the valid parentheses string "()(())". The second path shown results in the valid parentheses string "((()))". Note that there may be other valid parentheses string paths.
    ,
    # example 2
    [[[")", ")"], ["(", "("]]]
    # output: false
    # EXPLANATION:  The two possible paths form the parentheses strings "))(" and ")((". Since neither of them are valid parentheses strings, we return false.
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
### hasValidPath 
def cache(f): return f
from typing import *
def f_gold(grid: List[List[str]]) -> bool:
    @cache
    def dfs(i, j, t):
        if grid[i][j] == '(':
            t += 1
        else:
            t -= 1
        if t < 0:
            return False
        if i == m - 1 and j == n - 1:
            return t == 0
        for x, y in [(i + 1, j), (i, j + 1)]:
            if x < m and y < n and dfs(x, y, t):
                return True
        return False
    m, n = len(grid), len(grid[0])
    return dfs(0, 0, 0)
"-----------------"
test()

