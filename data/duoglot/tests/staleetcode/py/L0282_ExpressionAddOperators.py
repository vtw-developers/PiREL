
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    ["123", 6]
    # output: ["1*2*3","1+2+3"]
    # EXPLANATION:  Both "1*2*3" and "1+2+3" evaluate to 6.
    ,
    # example 2
    ["232", 8]
    # output: ["2*3+2","2+3*2"]
    # EXPLANATION:  Both "2*3+2" and "2+3*2" evaluate to 8.
    ,
    # example 3
    ["3456237490", 9191]
    # output: []
    # EXPLANATION:  There are no expressions that can be created from "3456237490" to evaluate to 9191.
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
### addOperators 
from typing import *
def f_gold(num: str, target: int) -> List[str]:
    ans = []
    def dfs(u, prev, curr, path):
        if u == len(num):
            if curr == target:
                ans.append(path)
            return
        for i in range(u, len(num)):
            if i != u and num[u] == '0':
                break
            next = int(num[u : i + 1])
            if u == 0:
                dfs(i + 1, next, next, path + str(next))
            else:
                dfs(i + 1, next, curr + next, path + "+" + str(next))
                dfs(i + 1, -next, curr - next, path + "-" + str(next))
                dfs(
                    i + 1,
                    prev * next,
                    curr - prev + prev * next,
                    path + "*" + str(next),
                )
    dfs(0, 0, 0, "")
    return ans
"-----------------"
test()

