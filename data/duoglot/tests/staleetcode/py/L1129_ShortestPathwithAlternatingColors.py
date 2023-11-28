
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [3, [[0, 1], [1, 2]], []]
    # output: [0,1,-1]
    ,
    # example 2
    [3, [[0, 1]], [[2, 1]]]
    # output: [0,1,-1]
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
### shortestAlternatingPaths 
from collections import deque
from collections import defaultdict
from typing import *
def f_gold(n: int, redEdges: List[List[int]], blueEdges: List[List[int]]
) -> List[int]:
    red = defaultdict(list)
    blue = defaultdict(list)
    for i, j in redEdges:
        red[i].append(j)
    for i, j in blueEdges:
        blue[i].append(j)
    vis_blue = [False] * n
    vis_red = [False] * n
    q = deque([(0, True), (0, False)])
    ans = [-1] * n
    d = -1
    while q:
        d += 1
        for _ in range(len(q)):
            i, b = q.popleft()
            if ans[i] == -1 or ans[i] > d:
                ans[i] = d
            vis = vis_blue if b else vis_red
            vis[i] = True
            ne = red[i] if b else blue[i]
            v = vis_red if b else vis_blue
            for j in ne:
                if not v[j]:
                    v[j] = True
                    q.append((j, not b))
    return ans
"-----------------"
test()

