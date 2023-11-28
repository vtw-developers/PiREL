
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [[1, 2, 1, 2, 1, 2, 1]]
    # output: true
    # EXPLANATION:  i = 1, j = 3, k = 5.  sum(0, i - 1) = sum(0, 0) = 1 sum(i + 1, j - 1) = sum(2, 2) = 1 sum(j + 1, k - 1) = sum(4, 4) = 1 sum(k + 1, n - 1) = sum(6, 6) = 1
    ,
    # example 2
    [[1, 2, 1, 2, 1, 2, 1, 2]]
    # output: false
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
### splitArray 
from typing import *
def f_gold(nums: List[int]) -> bool:
    n = len(nums)
    s = [0] * (n + 1)
    for i, v in enumerate(nums):
        s[i + 1] = s[i] + v
    for j in range(3, n - 3):
        seen = set()
        for i in range(1, j - 1):
            if s[i] == s[j] - s[i + 1]:
                seen.add(s[i])
        for k in range(j + 2, n - 1):
            if s[n] - s[k + 1] == s[k] - s[j + 1] and s[n] - s[k + 1] in seen:
                return True
    return False
"-----------------"
test()

