
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [[1, 3, 2, 2, 5, 2, 3, 7]]
    # output: 5
    # EXPLANATION:  The longest harmonious subsequence is [3,2,2,2,3].
    ,
    # example 2
    [[1, 2, 3, 4]]
    # output: 2
    ,
    # example 3
    [[1, 1, 1, 1]]
    # output: 0
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
### findLHS 
from collections import Counter
from typing import *
def f_gold(nums: List[int]) -> int:
    counter = Counter(nums)
    ans = 0
    for num in nums:
        if num + 1 in counter:
            ans = max(ans, counter[num] + counter[num + 1])
    return ans
"-----------------"
test()

