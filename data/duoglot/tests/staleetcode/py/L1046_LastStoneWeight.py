
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [[2, 7, 4, 1, 8, 1]]
    # output: 1
    # EXPLANATION:   We combine 7 and 8 to get 1 so the array converts to [2,4,1,1,1] then, we combine 2 and 4 to get 2 so the array converts to [2,1,1,1] then, we combine 2 and 1 to get 1 so the array converts to [1,1,1] then, we combine 1 and 1 to get 0 so the array converts to [1] then that's the value of the last stone.
    ,
    # example 2
    [[1]]
    # output: 1
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
### lastStoneWeight 
from heapq import heapify, heappush, heappop
from typing import *
def f_gold(stones: List[int]) -> int:
    h = [-s for s in stones]
    heapify(h)
    while len(h) > 1:
        y, x = -heappop(h), -heappop(h)
        if x != y:
            heappush(h, x - y)
    return 0 if not h else -h[0]
"-----------------"
test()

