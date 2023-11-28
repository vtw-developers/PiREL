
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [[3, 1, 4, 1, 5], 2]
    # output: 2
    # EXPLANATION:  There are two 2-diff pairs in the array, (1, 3) and (3, 5). Although we have two 1s in the input, we should only return the number of <strong>unique</strong> pairs.
    ,
    # example 2
    [[1, 2, 3, 4, 5], 1]
    # output: 4
    # EXPLANATION:  There are four 1-diff pairs in the array, (1, 2), (2, 3), (3, 4) and (4, 5).
    ,
    # example 3
    [[1, 3, 1, 5, 4], 0]
    # output: 1
    # EXPLANATION:  There is one 0-diff pair in the array, (1, 1).
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
### findPairs 
from typing import *
def f_gold(nums: List[int], k: int) -> int:
    vis, ans = set(), set()
    for v in nums:
        if v - k in vis:
            ans.add(v - k)
        if v + k in vis:
            ans.add(v)
        vis.add(v)
    return len(ans)
"-----------------"
test()

