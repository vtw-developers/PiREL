
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [[1, 1, 1, 2, 2, 3], 2]
    # output: [1,2]
    ,
    # example 2
    [[1], 1]
    # output: [1]
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
### topKFrequent 
from heapq import heapify, heappush, heappop
from collections import Counter
from typing import *
def f_gold(nums: List[int], k: int) -> List[int]:
    counter = Counter(nums)
    hp = []
    for num, freq in counter.items():
        if len(hp) == k:
            heappush(hp, (freq, num))
            heappop(hp)
        else:
            heappush(hp, (freq, num))
    return [t[1] for t in hp]
"-----------------"
test()

