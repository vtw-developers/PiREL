from L0794_ValidTicTacToeState import f_gold

##########
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [["O  ", "   ", "   "]]
    # output: false
    # EXPLANATION:  The first player always plays "X".
    ,
    # example 2
    [["XOX", " X ", "   "]]
    # output: false
    # EXPLANATION:  Players take turns making moves.
    ,
    # example 3
    [["XOX", "O O", "XOX"]]
    # output: true
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)

##########

test()
