
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [[1, 2, 3, 5, 2], [3, 2, 1, 4, 2]]
    # output: 7
    # EXPLANATION:  You can eat 7 apples: - On the first day, you eat an apple that grew on the first day. - On the second day, you eat an apple that grew on the second day. - On the third day, you eat an apple that grew on the second day. After this day, the apples that grew on the third day rot. - On the fourth to the seventh days, you eat apples that grew on the fourth day.
    ,
    # example 2
    [[3, 0, 0, 0, 0, 2], [3, 0, 0, 0, 0, 2]]
    # output: 5
    # EXPLANATION:  You can eat 5 apples: - On the first to the third day you eat apples that grew on the first day. - Do nothing on the fouth and fifth days. - On the sixth and seventh days you eat apples that grew on the sixth day.
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
### eatenApples 
from heapq import heapify, heappush, heappop
from typing import *
def f_gold(apples: List[int], days: List[int]) -> int:
    q = []
    n = len(apples)
    i = ans = 0
    while i < n or q:
        if i < n and apples[i] > 0:
            heappush(q, [i + days[i] - 1, apples[i]])
        while q and q[0][0] < i:
            heappop(q)
        if q:
            end, num = heappop(q)
            num -= 1
            ans += 1
            if num > 0 and end > i:
                heappush(q, [end, num])
        i += 1
    return ans
"-----------------"
test()

