
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [[1, 3, 5, 10, 15], [1, 2, 3, 4, 5]]
    # output: 34
    # EXPLANATION:  You can choose all the players.
    ,
    # example 2
    [[4, 5, 6, 5], [2, 1, 2, 1]]
    # output: 16
    # EXPLANATION:  It is best to choose the last 3 players. Notice that you are allowed to choose multiple people of the same age.
    ,
    # example 3
    [[1, 2, 3, 5], [8, 9, 10, 1]]
    # output: 6
    # EXPLANATION:  It is best to choose the first 3 players.
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
### bestTeamScore 
from typing import *
def f_gold(scores: List[int], ages: List[int]) -> int:
    nums = list(zip(ages, scores))
    nums.sort()
    n = len(nums)
    dp = [num[1] for num in nums]
    for i in range(n):
        for j in range(i):
            if nums[i][1] >= nums[j][1]:
                dp[i] = max(dp[i], dp[j] + nums[i][1])
    return max(dp)
"-----------------"
test()

