
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [[100, -23, -23, 404, 100, 23, 23, 23, 3, 404]]
    # output: 3
    # EXPLANATION:  You need three jumps from index 0 --> 4 --> 3 --> 9. Note that index 9 is the last index of the array.
    ,
    # example 2
    [[7]]
    # output: 0
    # EXPLANATION:  Start index is the last index. You do not need to jump.
    ,
    # example 3
    [[7, 6, 9, 6, 9, 6, 9, 7]]
    # output: 1
    # EXPLANATION:  You can jump directly from index 0 to index 7 which is last index of the array.
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
### minJumps 
from collections import deque
from collections import defaultdict
from typing import *
def f_gold(arr: List[int]) -> int:
    idx = defaultdict(list)
    for i, v in enumerate(arr):
        idx[v].append(i)
    q = deque([(0, 0)])
    vis = {0}
    while q:
        i, step = q.popleft()
        if i == len(arr) - 1:
            return step
        v = arr[i]
        step += 1
        for j in idx[v]:
            if j not in vis:
                vis.add(j)
                q.append((j, step))
        del idx[v]
        if i + 1 < len(arr) and (i + 1) not in vis:
            vis.add(i + 1)
            q.append((i + 1, step))
        if i - 1 >= 0 and (i - 1) not in vis:
            vis.add(i - 1)
            q.append((i - 1, step))
"-----------------"
test()

