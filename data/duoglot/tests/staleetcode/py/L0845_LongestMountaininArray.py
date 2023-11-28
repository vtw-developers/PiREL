
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [[2, 1, 4, 7, 3, 2, 5]]
    # output: 5
    # EXPLANATION:  The largest mountain is [1,4,7,3,2] which has length 5.
    ,
    # example 2
    [[2, 2, 2]]
    # output: 0
    # EXPLANATION:  There is no mountain.
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
### longestMountain 
from typing import *
def f_gold(arr: List[int]) -> int:
    left, right = 0, 1
    status = -1
    ans = 0
    while right < len(arr):
        if status == -1 or status == 1:
            if arr[right] == arr[right - 1]:
                status = -1
            if status == -1:
                if arr[right] > arr[right - 1]:
                    status = 1
                else:
                    left = right
            if status == 1 and arr[right] < arr[right - 1]:
                status = 2
        else:
            if arr[right] == arr[right - 1]:
                status = -1
                ans = max(ans, right - left)
                left = right
            elif arr[right] > arr[right - 1]:
                status = 1
                ans = max(ans, right - left)
                left = right - 1
        right += 1
    if status == 2:
        ans = max(right - left, ans)
    return ans
"-----------------"
test()

