
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [[[0, 2], [5, 10], [13, 23], [24, 25]], [[1, 5], [8, 12], [15, 24], [25, 26]]]
    # output: [[1,2],[5,5],[8,10],[15,23],[24,24],[25,25]]
    ,
    # example 2
    [[[1, 3], [5, 9]], []]
    # output: []
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
### intervalIntersection 
from typing import *
def f_gold(firstList: List[List[int]], secondList: List[List[int]]
) -> List[List[int]]:
    i = j = 0
    ans = []
    while i < len(firstList) and j < len(secondList):
        s1, e1, s2, e2 = *firstList[i], *secondList[j]
        l, r = max(s1, s2), min(e1, e2)
        if l <= r:
            ans.append([l, r])
        if e1 < e2:
            i += 1
        else:
            j += 1
    return ans
"-----------------"
test()

