from L0909_SnakesandLadders import f_gold

##########
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [[[-1, -1, -1, -1, -1, -1], [-1, -1, -1, -1, -1, -1], [-1, -1, -1, -1, -1, -1], [-1, 35, -1, -1, 13, -1], [-1, -1, -1, -1, -1, -1], [-1, 15, -1, -1, -1, -1]]]
    # output: 4
    # EXPLANATION:   In the beginning, you start at square 1 (at row 5, column 0). You decide to move to square 2 and must take the ladder to square 15. You then decide to move to square 17 and must take the snake to square 13. You then decide to move to square 14 and must take the ladder to square 35. You then decide to move to square 36, ending the game. This is the lowest possible number of moves to reach the last square, so return 4.
    ,
    # example 2
    [[[-1, -1], [-1, 3]]]
    # output: 1
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)

##########

test()
