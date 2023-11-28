
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [5]
    # output: [-7,-1,1,3,4]
    # EXPLANATION:  These arrays also are accepted [-5,-1,1,2,3] , [-3,-1,2,-2,4].
    ,
    # example 2
    [3]
    # output: [-1,0,1]
    ,
    # example 3
    [1]
    # output: [0]
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
### sumZero 
from typing import *
def f_gold(n: int) -> List[int]:
    presum = 0
    res = []
    for i in range(1, n):
        res.append(i)
        presum += i
    res.append(-presum)
    return res
"-----------------"
test()

