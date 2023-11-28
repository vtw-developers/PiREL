
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [[[2, 8], [6, 3], [8, 6]], 5, 4]
    # output: 9
    # EXPLANATION:   The optimal way is to: - Move right to position 6 and harvest 3 fruits - Move right to position 8 and harvest 6 fruits You moved 3 steps and harvested 3 + 6 = 9 fruits in total.
    ,
    # example 2
    [[[0, 9], [4, 1], [5, 7], [6, 2], [7, 4], [10, 9]], 5, 4]
    # output: 14
    # EXPLANATION:   You can move at most k = 4 steps, so you cannot reach position 0 nor 10. The optimal way is to: - Harvest the 7 fruits at the starting position 5 - Move left to position 4 and harvest 1 fruit - Move right to position 6 and harvest 2 fruits - Move right to position 7 and harvest 4 fruits You moved 1 + 3 = 4 steps and harvested 7 + 1 + 2 + 4 = 14 fruits in total.
    ,
    # example 3
    [[[0, 3], [6, 4], [8, 5]], 3, 2]
    # output: 0
    # EXPLANATION:  You can move at most k = 2 steps and cannot reach any position with fruits.
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
### maxTotalFruits 
from collections import deque
from typing import *
def f_gold(fruits: List[List[int]], startPos: int, k: int) -> int:
    q = deque()
    i, n = 0, len(fruits)
    ans = 0
    while i < n and fruits[i][0] <= startPos:
        if startPos - fruits[i][0] <= k:
            ans += fruits[i][1]
            q.append(fruits[i])
        i += 1
    t = ans
    while i < n and fruits[i][0] - startPos <= k:
        while (
            q
            and q[0][0] < startPos
            and fruits[i][0]
            - q[0][0]
            + min(startPos - q[0][0], fruits[i][0] - startPos)
            > k
        ):
            t -= q[0][1]
            q.popleft()
        t += fruits[i][1]
        ans = max(ans, t)
        i += 1
    return ans
"-----------------"
test()

