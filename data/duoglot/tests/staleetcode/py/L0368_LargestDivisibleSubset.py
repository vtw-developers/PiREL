
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [[1, 2, 3]]
    # output: [1,2]
    # EXPLANATION:  [1,3] is also accepted.
    ,
    # example 2
    [[1, 2, 4, 8]]
    # output: [1,2,4,8]
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
### largestDivisibleSubset 
from typing import *
def f_gold(nums: List[int]) -> List[int]:
    nums.sort()
    n = len(nums)
    f, p = [0] * n, [0] * n
    for i in range(n):
        l, pre = 1, i
        for j in range(n):
            if nums[i] % nums[j] == 0 and f[j] + 1 > l:
                l = f[j] + 1
                pre = j
        f[i] = l
        p[i] = pre
    max_len, max_index = 0, 0
    for i, v in enumerate(f):
        if max_len < v:
            max_len = v
            max_index = i
    ans = []
    while len(ans) < max_len:
        ans.append(nums[max_index])
        max_index = p[max_index]
    return ans[::-1]
"-----------------"
test()

