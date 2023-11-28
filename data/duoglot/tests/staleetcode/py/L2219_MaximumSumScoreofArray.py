
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [[4, 3, -2, 5]]
    # output: 10
    # EXPLANATION:  The sum score at index 0 is max(4, 4 + 3 + -2 + 5) = max(4, 10) = 10. The sum score at index 1 is max(4 + 3, 3 + -2 + 5) = max(7, 6) = 7. The sum score at index 2 is max(4 + 3 + -2, -2 + 5) = max(5, 3) = 5. The sum score at index 3 is max(4 + 3 + -2 + 5, 5) = max(10, 5) = 10. The maximum sum score of nums is 10.
    ,
    # example 2
    [[-3, -5]]
    # output: -3
    # EXPLANATION:  The sum score at index 0 is max(-3, -3 + -5) = max(-3, -8) = -3. The sum score at index 1 is max(-3 + -5, -5) = max(-8, -5) = -5. The maximum sum score of nums is -3.
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
### maximumSumScore 
from itertools import accumulate
from typing import *
def f_gold(nums: List[int]) -> int:
    s = [0] + list(accumulate(nums))
    return max(max(s[i + 1], s[-1] - s[i]) for i in range(len(nums)))
"-----------------"
test()

