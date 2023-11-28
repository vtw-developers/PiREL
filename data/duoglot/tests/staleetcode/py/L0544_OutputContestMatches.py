
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [4]
    # output: "((1,4),(2,3))"
    # EXPLANATION:  In the first round, we pair the team 1 and 4, the teams 2 and 3 together, as we need to make the strong team and weak team together. And we got (1, 4),(2, 3). In the second round, the winners of (1, 4) and (2, 3) need to play again to generate the final winner, so you need to add the paratheses outside them. And we got the final answer ((1,4),(2,3)).
    ,
    # example 2
    [8]
    # output: "(((1,8),(4,5)),((2,7),(3,6)))"
    # EXPLANATION:  First round: (1, 8),(2, 7),(3, 6),(4, 5) Second round: ((1, 8),(4, 5)),((2, 7),(3, 6)) Third round: (((1, 8),(4, 5)),((2, 7),(3, 6))) Since the third round will generate the final winner, you need to output the answer (((1,8),(4,5)),((2,7),(3,6))).
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
### findContestMatch 
from typing import *
def f_gold(n: int) -> str:
    team = [str(i + 1) for i in range(n)]
    while n > 1:
        for i in range(n >> 1):
            team[i] = f'({team[i]},{team[n - 1 - i]})'
        n >>= 1
    return team[0]
"-----------------"
test()

