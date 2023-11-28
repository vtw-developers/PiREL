
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [[3, 2, 4, 6]]
    # output: 7
    # EXPLANATION:  Apply the operation with x = 4 and i = 3, num[3] = 6 AND (6 XOR 4) = 6 AND 2 = 2. Now, nums = [3, 2, 4, 2] and the bitwise XOR of all the elements = 3 XOR 2 XOR 4 XOR 2 = 7. It can be shown that 7 is the maximum possible bitwise XOR. Note that other operations may be used to achieve a bitwise XOR of 7.
    ,
    # example 2
    [[1, 2, 3, 9, 2]]
    # output: 11
    # EXPLANATION:  Apply the operation zero times. The bitwise XOR of all the elements = 1 XOR 2 XOR 3 XOR 9 XOR 2 = 11. It can be shown that 11 is the maximum possible bitwise XOR.
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
### maximumXOR 
from typing import *
def f_gold(nums: List[int]) -> int:
    ans = 0
    for v in nums:
        ans |= v
    return ans
"-----------------"
test()

