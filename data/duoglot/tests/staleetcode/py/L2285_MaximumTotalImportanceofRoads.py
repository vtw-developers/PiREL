
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [5, [[0, 1], [1, 2], [2, 3], [0, 2], [1, 3], [2, 4]]]
    # output: 43
    # EXPLANATION:  The figure above shows the country and the assigned values of [2,4,5,3,1]. - The road (0,1) has an importance of 2 + 4 = 6. - The road (1,2) has an importance of 4 + 5 = 9. - The road (2,3) has an importance of 5 + 3 = 8. - The road (0,2) has an importance of 2 + 5 = 7. - The road (1,3) has an importance of 4 + 3 = 7. - The road (2,4) has an importance of 5 + 1 = 6. The total importance of all roads is 6 + 9 + 8 + 7 + 7 + 6 = 43. It can be shown that we cannot obtain a greater total importance than 43.
    ,
    # example 2
    [5, [[0, 3], [2, 4], [1, 3]]]
    # output: 20
    # EXPLANATION:  The figure above shows the country and the assigned values of [4,3,2,5,1]. - The road (0,3) has an importance of 4 + 5 = 9. - The road (2,4) has an importance of 2 + 1 = 3. - The road (1,3) has an importance of 3 + 5 = 8. The total importance of all roads is 9 + 3 + 8 = 20. It can be shown that we cannot obtain a greater total importance than 20.
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
### maximumImportance 
from typing import *
def f_gold(n: int, roads: List[List[int]]) -> int:
    deg = [0] * n
    for a, b in roads:
        deg[a] += 1
        deg[b] += 1
    deg.sort()
    return sum(i * v for i, v in enumerate(deg, 1))
"-----------------"
test()

