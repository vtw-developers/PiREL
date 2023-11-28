
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [[3, 3, 3, 3, 3, 1, 3]]
    # output: [[5],[0,1,2],[3,4,6]]
    # EXPLANATION:   The first group is [5]. The size is 1, and groupSizes[5] = 1. The second group is [0,1,2]. The size is 3, and groupSizes[0] = groupSizes[1] = groupSizes[2] = 3. The third group is [3,4,6]. The size is 3, and groupSizes[3] = groupSizes[4] = groupSizes[6] = 3. Other possible solutions are [[2,1,6],[5],[0,4,3]] and [[5],[0,6,2],[4,3,1]].
    ,
    # example 2
    [[2, 1, 3, 3, 3, 2]]
    # output: [[1],[0,5],[2,3,4]]
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
### groupThePeople 
from collections import defaultdict
from typing import *
def f_gold(groupSizes: List[int]) -> List[List[int]]:
    mp = defaultdict(list)
    for i, x in enumerate(groupSizes):
        mp[x].append(i)
    res = []
    for x, indexes in mp.items():
        l = len(indexes)
        for i in range(0, l, x):
            res.append(indexes[i : i + x])
    return res
"-----------------"
test()

