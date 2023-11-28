from L1275_FindWinneronaTicTacToeGame import f_gold

##########
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [[[0, 0], [2, 0], [1, 1], [2, 1], [2, 2]]]
    # output: "A"
    # EXPLANATION:  A wins, they always play first.
    ,
    # example 2
    [[[0, 0], [1, 1], [0, 1], [0, 2], [1, 0], [2, 0]]]
    # output: "B"
    # EXPLANATION:  B wins.
    ,
    # example 3
    [[[0, 0], [1, 1], [2, 0], [1, 0], [1, 2], [2, 1], [0, 1], [0, 2], [2, 2]]]
    # output: "Draw"
    # EXPLANATION:  The game ends in a draw since there are no moves to make.
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)

##########

test()
