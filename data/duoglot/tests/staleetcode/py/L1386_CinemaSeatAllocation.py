
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [3, [[1, 2], [1, 3], [1, 8], [2, 6], [3, 1], [3, 10]]]
    # output: 4
    # EXPLANATION:  The figure above shows the optimal allocation for four groups, where seats mark with blue are already reserved and contiguous seats mark with orange are for one group.
    ,
    # example 2
    [2, [[2, 1], [1, 8], [2, 6]]]
    # output: 2
    ,
    # example 3
    [4, [[4, 3], [1, 4], [4, 6], [1, 7]]]
    # output: 4
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
### maxNumberOfFamilies 
from collections import defaultdict
from typing import *
def f_gold(n: int, reservedSeats: List[List[int]]) -> int:
    m = defaultdict(int)
    for i, j in reservedSeats:
        m[i] = m[i] | (1 << (10 - j))
    masks = (0b0111100000, 0b0000011110, 0b0001111000)
    ans = (n - len(m)) << 1
    for v in m.values():
        for mask in masks:
            if (v & mask) == 0:
                v |= mask
                ans += 1
    return ans
"-----------------"
test()

