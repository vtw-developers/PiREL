
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    ["dcab", [[0, 3], [1, 2]]]
    # output: "bacd"<strong>Explaination:</strong> Swap s[0] and s[3], s = "bcad"Swap s[1] and s[2], s = "bacd"
    ,
    # example 2
    ["dcab", [[0, 3], [1, 2], [0, 2]]]
    # output: "abcd"<strong>Explaination: </strong>Swap s[0] and s[3], s = "bcad"Swap s[0] and s[2], s = "acbd"Swap s[1] and s[2], s = "abcd"
    ,
    # example 3
    ["cba", [[0, 1], [1, 2]]]
    # output: "abc"<strong>Explaination: </strong>Swap s[0] and s[1], s = "bca"Swap s[1] and s[2], s = "bac"Swap s[0] and s[1], s = "abc"
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
### smallestStringWithSwaps 
from heapq import heapify, heappush, heappop
from collections import defaultdict
from typing import *
def f_gold(s: str, pairs: List[List[int]]) -> str:
    def find(x):
        if p[x] != x:
            p[x] = find(p[x])
        return p[x]
    n = len(s)
    p = list(range(n))
    for a, b in pairs:
        p[find(a)] = find(b)
    mp = defaultdict(list)
    for i, c in enumerate(s):
        heappush(mp[find(i)], c)
    return ''.join(heappop(mp[find(i)]) for i in range(n))
"-----------------"
test()

