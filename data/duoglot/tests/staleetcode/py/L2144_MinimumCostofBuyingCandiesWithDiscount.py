
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [[1, 2, 3]]
    # output: 5
    # EXPLANATION:  We buy the candies with costs 2 and 3, and take the candy with cost 1 for free. The total cost of buying all candies is 2 + 3 = 5. This is the <strong>only</strong> way we can buy the candies. Note that we cannot buy candies with costs 1 and 3, and then take the candy with cost 2 for free. The cost of the free candy has to be less than or equal to the minimum cost of the purchased candies.
    ,
    # example 2
    [[6, 5, 7, 9, 2, 2]]
    # output: 23
    # EXPLANATION:  The way in which we can get the minimum cost is described below: - Buy candies with costs 9 and 7 - Take the candy with cost 6 for free - We buy candies with costs 5 and 2 - Take the last remaining candy with cost 2 for free Hence, the minimum cost to buy all candies is 9 + 7 + 5 + 2 = 23.
    ,
    # example 3
    [[5, 5]]
    # output: 10
    # EXPLANATION:  Since there are only 2 candies, we buy both of them. There is not a third candy we can take for free. Hence, the minimum cost to buy all candies is 5 + 5 = 10.
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
### minimumCost 
from typing import *
def f_gold(cost: List[int]) -> int:
    cost.sort()
    ans, n = 0, len(cost)
    for i in range(n - 1, -1, -3):
        ans += cost[i]
        if i >= 1:
            ans += cost[i - 1]
    return ans
"-----------------"
test()

