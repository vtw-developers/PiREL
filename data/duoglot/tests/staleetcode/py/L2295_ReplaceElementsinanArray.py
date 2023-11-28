
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [[1, 2, 4, 6], [[1, 3], [4, 7], [6, 1]]]
    # output: [3,2,7,1]
    # EXPLANATION:  We perform the following operations on nums: - Replace the number 1 with 3. nums becomes [<u><strong>3</strong></u>,2,4,6]. - Replace the number 4 with 7. nums becomes [3,2,<u><strong>7</strong></u>,6]. - Replace the number 6 with 1. nums becomes [3,2,7,<u><strong>1</strong></u>]. We return the final array [3,2,7,1].
    ,
    # example 2
    [[1, 2], [[1, 3], [2, 1], [3, 2]]]
    # output: [2,1]
    # EXPLANATION:  We perform the following operations to nums: - Replace the number 1 with 3. nums becomes [<u><strong>3</strong></u>,2]. - Replace the number 2 with 1. nums becomes [3,<u><strong>1</strong></u>]. - Replace the number 3 with 2. nums becomes [<u><strong>2</strong></u>,1]. We return the array [2,1].
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
### arrayChange 
from typing import *
def f_gold(nums: List[int], operations: List[List[int]]) -> List[int]:
    d = {v: i for i, v in enumerate(nums)}
    for a, b in operations:
        idx = d[a]
        d.pop(a)
        d[b] = idx
    ans = [0] * len(nums)
    for v, i in d.items():
        ans[i] = v
    return ans
"-----------------"
test()

