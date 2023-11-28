
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [[1, 7, 11], [2, 4, 6], 3]
    # output: [[1,2],[1,4],[1,6]]
    # EXPLANATION:  The first 3 pairs are returned from the sequence: [1,2],[1,4],[1,6],[7,2],[7,4],[11,2],[7,6],[11,4],[11,6]
    ,
    # example 2
    [[1, 1, 2], [1, 2, 3], 2]
    # output: [[1,1],[1,1]]
    # EXPLANATION:  The first 2 pairs are returned from the sequence: [1,1],[1,1],[1,2],[2,1],[1,2],[2,2],[1,3],[1,3],[2,3]
    ,
    # example 3
    [[1, 2], [3], 3]
    # output: [[1,3],[2,3]]
    # EXPLANATION:  All possible pairs are returned from the sequence: [1,3],[2,3]
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
### kSmallestPairs 
from heapq import heapify, heappush, heappop
from typing import *
def f_gold(nums1: List[int], nums2: List[int], k: int
) -> List[List[int]]:
    q = [[u + nums2[0], i, 0] for i, u in enumerate(nums1[:k])]
    heapify(q)
    ans = []
    while q and k > 0:
        _, i, j = heappop(q)
        ans.append([nums1[i], nums2[j]])
        k -= 1
        if j + 1 < len(nums2):
            heappush(q, [nums1[i] + nums2[j + 1], i, j + 1])
    return ans
"-----------------"
test()

