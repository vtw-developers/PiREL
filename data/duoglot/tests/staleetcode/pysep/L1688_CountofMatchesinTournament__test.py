from L1688_CountofMatchesinTournament import f_gold

##########
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [7]
    # output: 6
    # EXPLANATION:  Details of the tournament:  - 1st Round: Teams = 7, Matches = 3, and 4 teams advance. - 2nd Round: Teams = 4, Matches = 2, and 2 teams advance. - 3rd Round: Teams = 2, Matches = 1, and 1 team is declared the winner. Total number of matches = 3 + 2 + 1 = 6.
    ,
    # example 2
    [14]
    # output: 13
    # EXPLANATION:  Details of the tournament: - 1st Round: Teams = 14, Matches = 7, and 7 teams advance. - 2nd Round: Teams = 7, Matches = 3, and 4 teams advance. - 3rd Round: Teams = 4, Matches = 2, and 2 teams advance. - 4th Round: Teams = 2, Matches = 1, and 1 team is declared the winner. Total number of matches = 7 + 3 + 2 + 1 = 13.
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)

##########

test()
