
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    ["AACCGGTT", "AACCGGTA", ["AACCGGTA"]]
    # output: 1
    ,
    # example 2
    ["AACCGGTT", "AAACGGTA", ["AACCGGTA", "AACCGCTA", "AAACGGTA"]]
    # output: 2
    ,
    # example 3
    ["AAAAACCC", "AACCCCCC", ["AAAACCCC", "AAACCCCC", "AACCCCCC"]]
    # output: 3
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
### minMutation 
from collections import deque
from typing import *
def f_gold(start: str, end: str, bank: List[str]) -> int:
    s = set(bank)
    q = deque([(start, 0)])
    mp = {'A': 'TCG', 'T': 'ACG', 'C': 'ATG', 'G': 'ATC'}
    while q:
        t, step = q.popleft()
        if t == end:
            return step
        for i, v in enumerate(t):
            for j in mp[v]:
                next = t[:i] + j + t[i + 1 :]
                if next in s:
                    q.append((next, step + 1))
                    s.remove(next)
    return -1
"-----------------"
test()

