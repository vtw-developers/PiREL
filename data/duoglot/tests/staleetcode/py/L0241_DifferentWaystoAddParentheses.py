
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    ["2-1-1"]
    # output: [0,2]
    # EXPLANATION:  ((2-1)-1) = 0  (2-(1-1)) = 2
    ,
    # example 2
    ["2*3-4*5"]
    # output: [-34,-14,-10,-10,10]
    # EXPLANATION:  (2*(3-(4*5))) = -34  ((2*3)-(4*5)) = -14  ((2*(3-4))*5) = -10  (2*((3-4)*5)) = -10  (((2*3)-4)*5) = 10
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
### diffWaysToCompute 
def cache(f): return f
from typing import *
def f_gold(expression: str) -> List[int]:
    @cache
    def dfs(exp):
        if exp.isdigit():
            return [int(exp)]
        ans = []
        for i, c in enumerate(exp):
            if c in '-+*':
                left, right = dfs(exp[:i]), dfs(exp[i + 1:])
                for a in left:
                    for b in right:
                        if c == '-':
                            ans.append(a - b)
                        elif c == '+':
                            ans.append(a + b)
                        else:
                            ans.append(a * b)
        return ans
    return dfs(expression)
"-----------------"
test()

