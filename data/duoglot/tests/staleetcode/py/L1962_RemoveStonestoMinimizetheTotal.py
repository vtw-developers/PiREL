
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [[5, 4, 9], 2]
    # output: 12
    # EXPLANATION:  Steps of a possible scenario are: - Apply the operation on pile 2. The resulting piles are [5,4,<u>5</u>]. - Apply the operation on pile 0. The resulting piles are [<u>3</u>,4,5]. The total number of stones in [3,4,5] is 12.
    ,
    # example 2
    [[4, 3, 6, 7], 3]
    # output: 12
    # EXPLANATION:  Steps of a possible scenario are: - Apply the operation on pile 2. The resulting piles are [4,3,<u>3</u>,7]. - Apply the operation on pile 3. The resulting piles are [4,3,3,<u>4</u>]. - Apply the operation on pile 0. The resulting piles are [<u>2</u>,3,3,4]. The total number of stones in [2,3,3,4] is 12.
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
### minStoneSum 
from heapq import heapify, heappush, heappop
from typing import *
def f_gold(piles: List[int], k: int) -> int:
    h = []
    for p in piles:
        heappush(h, -p)
    for _ in range(k):
        p = -heappop(h)
        heappush(h, -((p + 1) >> 1))
    return -sum(h)
"-----------------"
test()

