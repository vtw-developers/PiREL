
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [[4, 14, 2]]
    # output: 6
    # EXPLANATION:  In binary representation, the 4 is 0100, 14 is 1110, and 2 is 0010 (just showing the four bits relevant in this case). The answer will be: HammingDistance(4, 14) + HammingDistance(4, 2) + HammingDistance(14, 2) = 2 + 2 + 2 = 6.
    ,
    # example 2
    [[4, 14, 4]]
    # output: 4
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
### totalHammingDistance 
from typing import *
def f_gold(nums: List[int]) -> int:
    ans = 0
    for i in range(31):
        a = b = 0
        for v in nums:
            t = (v >> i) & 1
            if t:
                a += 1
            else:
                b += 1
        ans += a * b
    return ans
"-----------------"
test()

