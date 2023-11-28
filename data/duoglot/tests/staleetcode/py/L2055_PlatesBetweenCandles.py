
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    ["**|**|***|", [[2, 5], [5, 9]]]
    # output: [2,3]
    # EXPLANATION:  - queries[0] has two plates between candles. - queries[1] has three plates between candles.
    ,
    # example 2
    ["***|**|*****|**||**|*", [[1, 17], [4, 5], [14, 17], [5, 11], [15, 16]]]
    # output: [9,0,0,0,0]
    # EXPLANATION:  - queries[0] has nine plates between candles. - The other queries have zero plates between candles.
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
### platesBetweenCandles 
from typing import *
def f_gold(s: str, queries: List[List[int]]) -> List[int]:
    n = len(s)
    presum = [0] * (n + 1)
    for i, c in enumerate(s):
        presum[i + 1] = presum[i] + (c == '*')
    left, right = [0] * n, [0] * n
    l = r = -1
    for i, c in enumerate(s):
        if c == '|':
            l = i
        left[i] = l
    for i in range(n - 1, -1, -1):
        if s[i] == '|':
            r = i
        right[i] = r
    ans = [0] * len(queries)
    for k, (l, r) in enumerate(queries):
        i, j = right[l], left[r]
        if i >= 0 and j >= 0 and i < j:
            ans[k] = presum[j] - presum[i + 1]
    return ans
"-----------------"
test()

