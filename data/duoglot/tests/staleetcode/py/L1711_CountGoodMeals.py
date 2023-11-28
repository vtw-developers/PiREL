
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [[1, 3, 5, 7, 9]]
    # output: 4
    # EXPLANATION: The good meals are (1,3), (1,7), (3,5) and, (7,9). Their respective sums are 4, 8, 8, and 16, all of which are powers of 2.
    ,
    # example 2
    [[1, 1, 1, 3, 3, 3, 7]]
    # output: 15
    # EXPLANATION: The good meals are (1,1) with 3 ways, (1,3) with 9 ways, and (1,7) with 3 ways.
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
### countPairs 
from collections import defaultdict
from typing import *
def f_gold(deliciousness: List[int]) -> int:
    mod = 1000000007
    limit = max(deliciousness) * 2
    pairs = 0
    freq = defaultdict(int)
    for d in deliciousness:
        target = 1
        while target <= limit:
            pairs = (pairs + freq[target - d]) % mod
            target = target << 1
        freq[d] += 1
    return pairs
"-----------------"
test()

