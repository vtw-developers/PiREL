
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    ["2", "3"]
    # output: "6"
    ,
    # example 2
    ["123", "456"]
    # output: "56088"
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
### multiply 
from typing import *
def f_gold(num1: str, num2: str) -> str:
    def mul(b, i):
        j, t = m - 1, 0
        while j >= 0 or t:
            if j >= 0:
                a = int(num1[j])
                t += a * b
            res[i] += t % 10
            if res[i] >= 10:
                res[i] %= 10
                res[i + 1] += 1
            i, j = i + 1, j - 1
            t //= 10
    m, n = len(num1), len(num2)
    res = [0] * (m + n)
    for i in range(n):
        b = int(num2[n - 1 - i])
        mul(b, i)
    while len(res) > 1 and res[-1] == 0:
        res.pop()
    return ''.join([str(v) for v in res[::-1]])
"-----------------"
test()

