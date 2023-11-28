
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [[5, 4, 3, 2, 1]]
    # output: 1
    # EXPLANATION:  Splitting into two or more chunks will not return the required result. For example, splitting into [5, 4], [3, 2, 1] will result in [4, 5, 1, 2, 3], which isn't sorted.
    ,
    # example 2
    [[2, 1, 3, 4, 4]]
    # output: 4
    # EXPLANATION:  We can split into two chunks, such as [2, 1], [3, 4, 4]. However, splitting into [2, 1], [3], [4], [4] is the highest number of chunks possible.
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
    stk = []
    for v in arr:
        if not stk or v >= stk[-1]:
            stk.append(v)
        else:
            mx = stk.pop()
            while stk and stk[-1] > v:
                stk.pop()
            stk.append(mx)
    return len(stk)
"-----------------"
test()

