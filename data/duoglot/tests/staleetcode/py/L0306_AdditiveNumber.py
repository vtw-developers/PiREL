
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    ["112358"]
    # output: true
    # EXPLANATION:   The digits can form an additive sequence: 1, 1, 2, 3, 5, 8.  1 + 1 = 2, 1 + 2 = 3, 2 + 3 = 5, 3 + 5 = 8
    ,
    # example 2
    ["199100199"]
    # output: true
    # EXPLANATION:   The additive sequence is: 1, 99, 100, 199.  1 + 99 = 100, 99 + 100 = 199
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
### isAdditiveNumber 
from typing import *
def f_gold(num: str) -> bool:
    def dfs(a, b, num):
        if not num:
            return True
        if a + b > 0 and num[0] == '0':
            return False
        for i in range(1, len(num) + 1):
            if a + b == int(num[:i]):
                if dfs(b, a + b, num[i:]):
                    return True
        return False
    n = len(num)
    for i in range(1, n - 1):
        for j in range(i + 1, n):
            if i > 1 and num[0] == '0':
                break
            if j - i > 1 and num[i] == '0':
                continue
            if dfs(int(num[:i]), int(num[i:j]), num[j:]):
                return True
    return False
"-----------------"
test()

