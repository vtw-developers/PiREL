
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [[[50, 45, 20], [95, 37, 53], [45, 23, 12]]]
    # output: 190
    # EXPLANATION:  Cuboid 1 is placed on the bottom with the 53x37 side facing down with height 95. Cuboid 0 is placed next with the 45x20 side facing down with height 50. Cuboid 2 is placed next with the 23x12 side facing down with height 45. The total height is 95 + 50 + 45 = 190.
    ,
    # example 2
    [[[38, 25, 45], [76, 35, 3]]]
    # output: 76
    # EXPLANATION:  You can't place any of the cuboids on the other. We choose cuboid 1 and rotate it so that the 35x3 side is facing down and its height is 76.
    ,
    # example 3
    [[[7, 11, 17], [7, 17, 11], [11, 7, 17], [11, 17, 7], [17, 7, 11], [17, 11, 7]]]
    # output: 102
    # EXPLANATION:  After rearranging the cuboids, you can see that all cuboids have the same dimension. You can place the 11x7 side down on all cuboids so their heights are 17. The maximum height of stacked cuboids is 6 * 17 = 102.
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
### maxHeight 
from typing import *
def f_gold(cuboids: List[List[int]]) -> int:
    for c in cuboids:
        c.sort()
    cuboids.sort()
    n = len(cuboids)
    dp = [0] * n
    for i in range(n):
        for j in range(i):
            if cuboids[j][1] <= cuboids[i][1] and cuboids[j][2] <= cuboids[i][2]:
                dp[i] = max(dp[i], dp[j])
        dp[i] += cuboids[i][2]
    return max(dp)
"-----------------"
test()

