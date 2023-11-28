
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [[5, 7, 1, 4], 3]
    # output: [12,10,16,13]
    # EXPLANATION:  Each number is replaced by the sum of the next 3 numbers. The decrypted code is [7+1+4, 1+4+5, 4+5+7, 5+7+1]. Notice that the numbers wrap around.
    ,
    # example 2
    [[1, 2, 3, 4], 0]
    # output: [0,0,0,0]
    # EXPLANATION:  When k is zero, the numbers are replaced by 0.
    ,
    # example 3
    [[2, 4, 9, 3], -2]
    # output: [12,5,6,13]
    # EXPLANATION:  The decrypted code is [3+9, 2+3, 4+2, 9+4]. Notice that the numbers wrap around again. If k is negative, the sum is of the <strong>previous</strong> numbers.
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
### decrypt 
from typing import *
def f_gold(code: List[int], k: int) -> List[int]:
    n = len(code)
    res = [0] * n
    if k == 0:
        return res
    for i in range(n):
        if k > 0:
            for j in range(i + 1, i + k + 1):
                res[i] += code[j % n]
        else:
            for j in range(i + k, i):
                res[i] += code[(j + n) % n]
    return res
"-----------------"
test()

