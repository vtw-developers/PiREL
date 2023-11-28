
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [[100, 4, 200, 1, 3, 2]]
    # output: 4
    # EXPLANATION:  The longest consecutive elements sequence is <code>[1, 2, 3, 4]</code>. Therefore its length is 4.
    ,
    # example 2
    [[0, 3, 7, 2, 5, 8, 4, 6, 0, 1]]
    # output: 9
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
### longestConsecutive 
from typing import *
def f_gold(nums: List[int]) -> int:
    s, res = set(nums), 0
    for num in nums:
        if num - 1 not in s:
            t, next = 1, num + 1
            while next in s:
                t, next = t + 1, next + 1
            res = max(res, t)
    return res
"-----------------"
test()

