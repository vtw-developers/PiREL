
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [[1, 2, 3, 5], 3]
    # output: [2,5]
    # EXPLANATION:  The fractions to be considered in sorted order are: 1/5, 1/3, 2/5, 1/2, 3/5, and 2/3. The third fraction is 2/5.
    ,
    # example 2
    [[1, 7], 1]
    # output: [1,7]
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
### kthSmallestPrimeFraction 
from heapq import heapify, heappush, heappop
from typing import *
def f_gold(arr: List[int], k: int) -> List[int]:
    h = [(1 / y, 0, j + 1) for j, y in enumerate(arr[1:])]
    heapify(h)
    for _ in range(k - 1):
        _, i, j = heappop(h)
        if i + 1 < j:
            heappush(h, (arr[i + 1] / arr[j], i + 1, j))
    return [arr[h[0][1]], arr[h[0][2]]]
"-----------------"
test()

