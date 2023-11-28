
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [[[2, 1], [3, 4], [3, 2]]]
    # output: [1,2,3,4]
    # EXPLANATION:  This array has all its adjacent pairs in adjacentPairs. Notice that adjacentPairs[i] may not be in left-to-right order.
    ,
    # example 2
    [[[4, -2], [1, 4], [-3, 1]]]
    # output: [-2,4,1,-3]
    # EXPLANATION:  There can be negative numbers. Another solution is [-3,1,4,-2], which would also be accepted.
    ,
    # example 3
    [[[100000, -100000]]]
    # output: [100000,-100000]
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
### restoreArray 
from collections import defaultdict
from typing import *
def f_gold(adjacentPairs: List[List[int]]) -> List[int]:
    graph = defaultdict(list)
    for pair in adjacentPairs:
        graph[pair[0]].append(pair[1])
        graph[pair[1]].append(pair[0])
    ans = []
    vis = set()
    def dfs(idx):
        if idx in vis:
            return
        vis.add(idx)
        ans.append(idx)
        for nxt in graph[idx]:
            dfs(nxt)
    start = -1
    for idx, adj in graph.items():
        if len(adj) == 1:
            start = idx
            break
    dfs(start)
    return ans
"-----------------"
test()

