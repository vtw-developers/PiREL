
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [[1, 0, -1, 0, -2, 2], 0]
    # output: [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]
    ,
    # example 2
    [[2, 2, 2, 2, 2], 8]
    # output: [[2,2,2,2]]
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
### fourSum 
from typing import *
def f_gold(nums: List[int], target: int) -> List[List[int]]:
    n, res = len(nums), []
    if n < 4:
        return []
    nums.sort()
    for i in range(n - 3):
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        for j in range(i + 1, n - 2):
            if j > i + 1 and nums[j] == nums[j - 1]:
                continue
            k, l = j + 1, n - 1
            while k < l:
                if nums[i] + nums[j] + nums[k] + nums[l] == target:
                    res.append([nums[i], nums[j], nums[k], nums[l]])
                    k += 1
                    l -= 1
                    while k < n and nums[k] == nums[k - 1]:
                        k += 1
                    while l > j and nums[l] == nums[l + 1]:
                        l -= 1
                elif nums[i] + nums[j] + nums[k] + nums[l] < target:
                    k += 1
                else:
                    l -= 1
    return res
"-----------------"
test()

