
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [[["0", "0", "1", "0"], ["0", "1", "1", "0"], ["0", "1", "0", "0"]], 0, 2]
    # output: 6
    ,
    # example 2
    [[["1"]], 0, 0]
    # output: 1
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
### minArea 
from typing import *
def f_gold(image: List[List[str]], x: int, y: int) -> int:
    m, n = len(image), len(image[0])
    left, right = 0, x
    while left < right:
        mid = (left + right) >> 1
        c = 0
        while c < n and image[mid][c] == '0':
            c += 1
        if c < n:
            right = mid
        else:
            left = mid + 1
    u = left
    left, right = x, m - 1
    while left < right:
        mid = (left + right + 1) >> 1
        c = 0
        while c < n and image[mid][c] == '0':
            c += 1
        if c < n:
            left = mid
        else:
            right = mid - 1
    d = left
    left, right = 0, y
    while left < right:
        mid = (left + right) >> 1
        r = 0
        while r < m and image[r][mid] == '0':
            r += 1
        if r < m:
            right = mid
        else:
            left = mid + 1
    l = left
    left, right = y, n - 1
    while left < right:
        mid = (left + right + 1) >> 1
        r = 0
        while r < m and image[r][mid] == '0':
            r += 1
        if r < m:
            left = mid
        else:
            right = mid - 1
    r = left
    return (d - u + 1) * (r - l + 1)
"-----------------"
test()

