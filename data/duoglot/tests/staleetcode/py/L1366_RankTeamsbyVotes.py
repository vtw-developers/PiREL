
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [["ABC", "ACB", "ABC", "ACB", "ACB"]]
    # output: "ACB"
    # EXPLANATION:  Team A was ranked first place by 5 voters. No other team was voted as first place so team A is the first team. Team B was ranked second by 2 voters and was ranked third by 3 voters. Team C was ranked second by 3 voters and was ranked third by 2 voters. As most of the voters ranked C second, team C is the second team and team B is the third.
    ,
    # example 2
    [["WXYZ", "XYZW"]]
    # output: "XWYZ"
    # EXPLANATION:  X is the winner due to tie-breaking rule. X has same votes as W for the first position but X has one vote as second position while W doesn't have any votes as second position.
    ,
    # example 3
    [["ZMNAGUEDSJYLBOPHRQICWFXTVK"]]
    # output: "ZMNAGUEDSJYLBOPHRQICWFXTVK"
    # EXPLANATION:  Only one voter so his votes are used for the ranking.
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
### rankTeams 
from collections import defaultdict
from typing import *
def f_gold(votes: List[str]) -> str:
    d = defaultdict(lambda: [0] * len(votes[0]))
    for vote in votes:
        for i, v in enumerate(vote):
            d[v][i] -= 1
    ans = sorted(votes[0], key=lambda x: (d[x], x))
    return ''.join(ans)
"-----------------"
test()

