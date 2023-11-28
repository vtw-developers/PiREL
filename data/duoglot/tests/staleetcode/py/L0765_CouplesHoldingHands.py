
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [[0, 2, 1, 3]]
    # output: 1
    # EXPLANATION:  We only need to swap the second (row[1]) and third (row[2]) person.
    ,
    # example 2
    [[3, 2, 0, 1]]
    # output: 0
    # EXPLANATION:  All couples are already seated side by side.
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
### minSwapsCouples 
from typing import *
def f_gold(row: List[int]) -> int:
    n = len(row) >> 1
    p = list(range(n))
    def find(x):
        if p[x] != x:
            p[x] = find(p[x])
        return p[x]
    for i in range(0, len(row), 2):
        a, b = row[i] >> 1, row[i + 1] >> 1
        p[find(a)] = find(b)
    cnt = 0
    for i in range(n):
        if i == find(i):
            cnt += 1
    return n - cnt
"-----------------"
test()

