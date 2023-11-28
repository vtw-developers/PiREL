
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [3, [[0, 1, 2], [1, 2, 4], [2, 0, 8], [1, 0, 16]], [[0, 1, 2], [0, 2, 5]]]
    # output: [false,true]
    # EXPLANATION:  The above figure shows the given graph. Note that there are two overlapping edges between 0 and 1 with distances 2 and 16. For the first query, between 0 and 1 there is no path where each distance is less than 2, thus we return false for this query. For the second query, there is a path (0 -> 1 -> 2) of two edges with distances less than 5, thus we return true for this query.
    ,
    # example 2
    [5, [[0, 1, 10], [1, 2, 5], [2, 3, 9], [3, 4, 13]], [[0, 4, 14], [1, 4, 13]]]
    # output: [true,false]<strong>Exaplanation:</strong> The above figure shows the given graph.
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
### distanceLimitedPathsExist 
from typing import *
def f_gold(n: int, edgeList: List[List[int]], queries: List[List[int]]
) -> List[bool]:
    def find(x):
        if p[x] != x:
            p[x] = find(p[x])
        return p[x]
    p = list(range(n))
    edgeList.sort(key=lambda x: x[2])
    m = len(queries)
    indexes = list(range(m))
    indexes.sort(key=lambda i: queries[i][2])
    ans = [False] * m
    i = 0
    for j in indexes:
        pj, qj, limit = queries[j]
        while i < len(edgeList) and edgeList[i][2] < limit:
            u, v, _ = edgeList[i]
            p[find(u)] = find(v)
            i += 1
        ans[j] = find(pj) == find(qj)
    return ans
"-----------------"
test()

