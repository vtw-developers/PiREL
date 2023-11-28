
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [[[1, 2], [2, 3], [5], [0], [5], [], []]]
    # output: [2,4,5,6]
    # EXPLANATION:  The given graph is shown above. Nodes 5 and 6 are terminal nodes as there are no outgoing edges from either of them. Every path starting at nodes 2, 4, 5, and 6 all lead to either node 5 or 6.
    ,
    # example 2
    [[[1, 2, 3, 4], [1, 2], [3, 4], [0, 4], []]]
    # output: [4]
    # EXPLANATION:  Only node 4 is a terminal node, and every path starting at node 4 leads to node 4.
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
### eventualSafeNodes 
from collections import deque
from collections import defaultdict
from typing import *
def f_gold(graph: List[List[int]]) -> List[int]:
    n = len(graph)
    outDegree = [len(vs) for vs in graph]
    revGraph = defaultdict(list)
    for u, vs in enumerate(graph):
        for v in vs:
            revGraph[v].append(u)
    q = deque([i for i, d in enumerate(outDegree) if d == 0])
    while q:
        for u in revGraph[q.popleft()]:
            outDegree[u] -= 1
            if outDegree[u] == 0:
                q.append(u)
    return [i for i, d in enumerate(outDegree) if d == 0]
"-----------------"
test()

