
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [[4, 3, 2, 1, 0]]
    # output: 1
    # EXPLANATION:  Splitting into two or more chunks will not return the required result. For example, splitting into [4, 3], [2, 1, 0] will result in [3, 4, 0, 1, 2], which isn't sorted.
    ,
    # example 2
    [[1, 0, 2, 3, 4]]
    # output: 4
    # EXPLANATION:  We can split into two chunks, such as [1, 0], [2, 3, 4]. However, splitting into [1, 0], [2], [3], [4] is the highest number of chunks possible.
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
### maxChunksToSorted 
from typing import *
def f_gold(arr: List[int]) -> int:
    mx = ans = 0
    for i, v in enumerate(arr):
        mx = max(mx, v)
        if i == mx:
            ans += 1
    return ans
"-----------------"
test()

