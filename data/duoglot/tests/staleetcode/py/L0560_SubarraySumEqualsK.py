
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [[1, 1, 1], 2]
    # output: 2
    ,
    # example 2
    [[1, 2, 3], 3]
    # output: 2
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
### subarraySum 
from collections import Counter
from typing import *
def f_gold(nums: List[int], k: int) -> int:
    counter = Counter({0: 1})
    ans = s = 0
    for num in nums:
        s += num
        ans += counter[s - k]
        counter[s] += 1
    return ans
"-----------------"
test()

