
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [[[3, 2], [4, 3], [4, 4], [2, 5]]]
    # output: 5
    # EXPLANATION:  The maximum points can be earned by solving questions 0 and 3. - Solve question 0: Earn 3 points, will be unable to solve the next 2 questions - Unable to solve questions 1 and 2 - Solve question 3: Earn 2 points Total points earned: 3 + 2 = 5. There is no other way to earn 5 or more points.
    ,
    # example 2
    [[[1, 1], [2, 2], [3, 3], [4, 4], [5, 5]]]
    # output: 7
    # EXPLANATION:  The maximum points can be earned by solving questions 1 and 4. - Skip question 0 - Solve question 1: Earn 2 points, will be unable to solve the next 2 questions - Unable to solve questions 2 and 3 - Solve question 4: Earn 5 points Total points earned: 2 + 5 = 7. There is no other way to earn 7 or more points.
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
### mostPoints 
def cache(f): return f
from typing import *
def f_gold(questions: List[List[int]]) -> int:
    @cache
    def dfs(i):
        if i >= len(questions):
            return 0
        return max(questions[i][0] + dfs(i + questions[i][1] + 1), dfs(i + 1))
    return dfs(0)
"-----------------"
test()

