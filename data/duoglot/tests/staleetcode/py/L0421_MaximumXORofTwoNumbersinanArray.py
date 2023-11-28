
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [[3, 10, 5, 25, 2, 8]]
    # output: 28
    # EXPLANATION:  The maximum result is 5 XOR 25 = 28.
    ,
    # example 2
    [[14, 70, 53, 83, 49, 91, 36, 80, 92, 51, 66, 70]]
    # output: 127
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
### findMaximumXOR 
from typing import *
def f_gold(nums: List[int]) -> int:
    max = 0
    mask = 0
    for i in range(30, -1, -1):
        current = 1 << i
        mask = mask ^ current
        s = set()
        for num in nums:
            s.add(num & mask)
        flag = max | current
        for prefix in s:
            if prefix ^ flag in s:
                max = flag
                break
    return max
"-----------------"
test()

