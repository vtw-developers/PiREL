
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [[-1, 0, 1, 2, -1, -4]]
    # output: [[-1,-1,2],[-1,0,1]]
    ,
    # example 2
    [[]]
    # output: []
    ,
    # example 3
    [[0]]
    # output: []
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
### threeSum 
from typing import *
def f_gold(nums: List[int]) -> List[List[int]]:
    n, res = len(nums), []
    if n < 3:
        return res
    nums.sort()
    for i in range(n - 2):
        if nums[i] > 0:
            break
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        j, k = i + 1, n - 1
        while j < k:
            if nums[i] + nums[j] + nums[k] == 0:
                res.append([nums[i], nums[j], nums[k]])
                j += 1
                k -= 1
                while j < n and nums[j] == nums[j - 1]:
                    j += 1
                while k > i and nums[k] == nums[k + 1]:
                    k -= 1
            elif nums[i] + nums[j] + nums[k] < 0:
                j += 1
            else:
                k -= 1
    return res
"-----------------"
test()

