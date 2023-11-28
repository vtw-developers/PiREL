
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [1, 1]
    # output: 0
    # EXPLANATION:  row 1: <u>0</u>
    ,
    # example 2
    [2, 1]
    # output: 0
    # EXPLANATION:   row 1: 0 row 2: <u>0</u>1
    ,
    # example 3
    [2, 2]
    # output: 1
    # EXPLANATION:   row 1: 0 row 2: 0<u>1</u>
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
### kthGrammar 
from typing import *
def f_gold(n: int, k: int) -> int:
    if n == 1:
        return 0
    if k <= (1 << (n - 2)):
        return f_gold(n - 1, k)
    return f_gold(n - 1, k - (1 << (n - 2))) ^ 1
"-----------------"
test()

