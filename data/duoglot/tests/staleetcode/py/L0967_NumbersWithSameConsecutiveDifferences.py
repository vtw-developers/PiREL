
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [3, 7]
    # output: [181,292,707,818,929]
    # EXPLANATION:  Note that 070 is not a valid number, because it has leading zeroes.
    ,
    # example 2
    [2, 1]
    # output: [10,12,21,23,32,34,43,45,54,56,65,67,76,78,87,89,98]
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
### numsSameConsecDiff 
from typing import *
def f_gold(n: int, k: int) -> List[int]:
    ans = []
    def dfs(n, k, t):
        if n == 0:
            ans.append(t)
            return
        last = t % 10
        if last + k <= 9:
            dfs(n - 1, k, t * 10 + last + k)
        if last - k >= 0 and k != 0:
            dfs(n - 1, k, t * 10 + last - k)
    for i in range(1, 10):
        dfs(n - 1, k, i)
    return ans
"-----------------"
test()

