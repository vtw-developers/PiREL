
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [[10, 2, 5, 3]]
    # output: true
    # EXPLANATION:  N<code> = 10</code> is the double of M<code> = 5</code>,that is, <code>10 = 2 * 5</code>.
    ,
    # example 2
    [[7, 1, 14, 11]]
    # output: true
    # EXPLANATION:  N<code> = 14</code> is the double of M<code> = 7</code>,that is, <code>14 = 2 * 7</code>.
    ,
    # example 3
    [[3, 1, 7, 11]]
    # output: false
    # EXPLANATION:  In this case does not exist N and M, such that N = 2 * M.
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
### checkIfExist 
from typing import *
def f_gold(arr: List[int]) -> bool:
    m = {v: i for i, v in enumerate(arr)}
    return any(v << 1 in m and m[v << 1] != i for i, v in enumerate(arr))
"-----------------"
test()

