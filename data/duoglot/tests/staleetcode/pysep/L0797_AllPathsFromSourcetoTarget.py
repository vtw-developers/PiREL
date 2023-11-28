### allPathsSourceTarget 
from collections import deque
from typing import *
def f_gold(graph: List[List[int]]) -> List[List[int]]:
    n = len(graph)
    q = deque([[0]])
    ans = []
    while q:
        path = q.popleft()
        u = path[-1]
        if u == n - 1:
            ans.append(path)
            continue
        for v in graph[u]:
            q.append(path + [v])
    return ans