
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [[[1, 2], [2, 3]]]
    # output: 1
    # EXPLANATION:  There is exactly one valid rooted tree, which is shown in the above figure.
    ,
    # example 2
    [[[1, 2], [2, 3], [1, 3]]]
    # output: 2
    # EXPLANATION:  There are multiple valid rooted trees. Three of them are shown in the above figures.
    ,
    # example 3
    [[[1, 2], [2, 3], [2, 4], [1, 5]]]
    # output: 0
    # EXPLANATION:  There are no valid rooted trees.
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
### checkWays 
from collections import defaultdict
from typing import *
def f_gold(pairs: List[List[int]]) -> int:
    g = [[False] * 510 for _ in range(510)]
    v = defaultdict(list)
    for x, y in pairs:
        g[x][y] = g[y][x] = True
        v[x].append(y)
        v[y].append(x)
    nodes = []
    for i in range(510):
        if v[i]:
            nodes.append(i)
            g[i][i] = True
    nodes.sort(key=lambda x: len(v[x]))
    equal = False
    root = 0
    for i, x in enumerate(nodes):
        j = i + 1
        while j < len(nodes) and not g[x][nodes[j]]:
            j += 1
        if j < len(nodes):
            y = nodes[j]
            if len(v[x]) == len(v[y]):
                equal = True
            for z in v[x]:
                if not g[y][z]:
                    return 0
        else:
            root += 1
    if root > 1:
        return 0
    return 2 if equal else 1
"-----------------"
test()

