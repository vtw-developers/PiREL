
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [5]
    # output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]
    ,
    # example 2
    [1]
    # output: [[1]]
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
### generate 
from typing import *
def f_gold(numRows: int) -> List[List[int]]:
    ans = []
    for i in range(numRows):
        t = [
            1 if j == 0 or j == i else ans[-1][j] + ans[-1][j - 1]
            for j in range(i + 1)
        ]
        ans.append(t)
    return ans
"-----------------"
test()

