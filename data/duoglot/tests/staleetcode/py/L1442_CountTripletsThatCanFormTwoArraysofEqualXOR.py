
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [[2, 3, 1, 6, 7]]
    # output: 4
    # EXPLANATION:  The triplets are (0,1,2), (0,2,2), (2,3,4) and (2,4,4)
    ,
    # example 2
    [[1, 1, 1, 1, 1]]
    # output: 10
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
### countTriplets 
from typing import *
def f_gold(arr: List[int]) -> int:
    n = len(arr)
    pre = [0] * (n + 1)
    for i in range(n):
        pre[i + 1] = pre[i] ^ arr[i]
    ans = 0
    for i in range(n - 1):
        for j in range(i + 1, n):
            for k in range(j, n):
                a, b = pre[j] ^ pre[i], pre[k + 1] ^ pre[j]
                if a == b:
                    ans += 1
    return ans
"-----------------"
test()

