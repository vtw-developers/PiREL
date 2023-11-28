from L0773_SlidingPuzzle import f_gold

##########
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [[[1, 2, 3], [4, 0, 5]]]
    # output: 1
    # EXPLANATION:  Swap the 0 and the 5 in one move.
    ,
    # example 2
    [[[1, 2, 3], [5, 4, 0]]]
    # output: -1
    # EXPLANATION:  No number of moves will make the board solved.
    ,
    # example 3
    [[[4, 1, 2], [5, 0, 3]]]
    # output: 5
    # EXPLANATION:  5 is the smallest number of moves that solves the board. An example path: After move 0: [[4,1,2],[5,0,3]] After move 1: [[4,1,2],[0,5,3]] After move 2: [[0,1,2],[4,5,3]] After move 3: [[1,0,2],[4,5,3]] After move 4: [[1,2,0],[4,5,3]] After move 5: [[1,2,3],[4,5,0]]
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)

##########

test()
