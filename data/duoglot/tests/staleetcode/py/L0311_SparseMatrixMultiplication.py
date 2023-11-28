
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [[[1, 0, 0], [-1, 0, 3]], [[7, 0, 0], [0, 0, 0], [0, 0, 1]]]
    # output: [[7,0,0],[-7,0,3]]
    ,
    # example 2
    [[[0]], [[0]]]
    # output: [[0]]
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
### multiply 
from collections import defaultdict
from typing import *
def f_gold(mat1: List[List[int]], mat2: List[List[int]]) -> List[List[int]]:
    r1, c1, c2 = len(mat1), len(mat1[0]), len(mat2[0])
    res = [[0] * c2 for _ in range(r1)]
    mp = defaultdict(list)
    for i in range(r1):
        for j in range(c1):
            if mat1[i][j] != 0:
                mp[i].append(j)
    for i in range(r1):
        for j in range(c2):
            for k in mp[i]:
                res[i][j] += mat1[i][k] * mat2[k][j]
    return res
"-----------------"
test()

