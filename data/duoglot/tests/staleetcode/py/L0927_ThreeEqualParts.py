
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [[1, 0, 1, 0, 1]]
    # output: [0,3]
    ,
    # example 2
    [[1, 1, 0, 1, 1]]
    # output: [-1,-1]
    ,
    # example 3
    [[1, 1, 0, 0, 1]]
    # output: [0,2]
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
### threeEqualParts 
from typing import *
def f_gold(arr: List[int]) -> List[int]:
    def find(cnt):
        s = 0
        for i, v in enumerate(arr):
            s += v
            if s == cnt:
                return i
        return -1
    n = len(arr)
    cnt, mod = divmod(sum(arr), 3)
    if mod:
        return [-1, -1]
    if cnt == 0:
        return [0, n - 1]
    i = find(1)
    j = find(cnt + 1)
    k = find(cnt * 2 + 1)
    while k < n and arr[i] == arr[j] == arr[k]:
        i, j, k = i + 1, j + 1, k + 1
    if k == n:
        return [i - 1, j]
    return [-1, -1]
"-----------------"
test()

