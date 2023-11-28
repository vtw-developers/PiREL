
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [[[1, 0], [0, 3]], [0, 1]]
    # output: true
    # EXPLANATION:  You can reach the destination (0, 1) after 1 turn, while the ghosts located at (1, 0) and (0, 3) cannot catch up with you.
    ,
    # example 2
    [[[1, 0]], [2, 0]]
    # output: false
    # EXPLANATION:  You need to reach the destination (2, 0), but the ghost at (1, 0) lies between you and the destination.
    ,
    # example 3
    [[[2, 0]], [1, 0]]
    # output: false
    # EXPLANATION:  The ghost can reach the target at the same time as you.
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
### escapeGhosts 
from typing import *
def f_gold(ghosts, target):
    """
    :type ghosts: List[List[int]]
    :type target: List[int]
    :rtype: bool
    """
    flag = abs(target[0]) + abs(target[1])
    for i in ghosts:
        if abs(i[0] - target[0]) + abs(i[1] - target[1]) <= flag:
            return False
    else:
        return True
"-----------------"
test()

