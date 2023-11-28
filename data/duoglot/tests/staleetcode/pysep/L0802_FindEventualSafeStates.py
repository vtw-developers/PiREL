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