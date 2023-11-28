
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [[3, 0, 6, 1, 5]]
    # output: 3
    # EXPLANATION:  [3,0,6,1,5] means the researcher has 5 papers in total and each of them had received 3, 0, 6, 1, 5 citations respectively. Since the researcher has 3 papers with at least 3 citations each and the remaining two with no more than 3 citations each, their h-index is 3.
    ,
    # example 2
    [[1, 3, 1]]
    # output: 1
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
### hIndex 
from typing import *
def f_gold(citations: List[int]) -> int:
    n = len(citations)
    cnt = [0] * (n + 1)
    for c in citations:
        if c <= n:
            cnt[c] += 1
        else:
            cnt[n] += 1
    sum = 0
    for i in range(n, -1, -1):
        sum += cnt[i]
        if sum >= i:
            return i
    return 0
"-----------------"
test()

