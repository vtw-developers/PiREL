from L1222_QueensThatCanAttacktheKing import f_gold

##########
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [[[0, 1], [1, 0], [4, 0], [0, 4], [3, 3], [2, 4]], [0, 0]]
    # output: [[0,1],[1,0],[3,3]]
    # EXPLANATION:     The queen at [0,1] can attack the king cause they're in the same row.   The queen at [1,0] can attack the king cause they're in the same column.   The queen at [3,3] can attack the king cause they're in the same diagnal.   The queen at [0,4] can't attack the king cause it's blocked by the queen at [0,1].   The queen at [4,0] can't attack the king cause it's blocked by the queen at [1,0].   The queen at [2,4] can't attack the king cause it's not in the same row/column/diagnal as the king.
    ,
    # example 2
    [[[0, 0], [1, 1], [2, 2], [3, 4], [3, 5], [4, 4], [4, 5]], [3, 3]]
    # output: [[2,2],[3,4],[4,4]]
    ,
    # example 3
    [[[5, 6], [7, 7], [2, 1], [0, 7], [1, 6], [5, 1], [3, 7], [0, 3], [4, 0], [1, 2], [6, 3], [5, 0], [0, 4], [2, 2], [1, 1], [6, 4], [5, 4], [0, 0], [2, 6], [4, 5], [5, 2], [1, 4], [7, 5], [2, 3], [0, 5], [4, 2], [1, 0], [2, 7], [0, 1], [4, 6], [6, 1], [0, 6], [4, 3], [1, 7]], [3, 4]]
    # output: [[2,3],[1,4],[1,6],[3,7],[4,3],[5,4],[4,5]]
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)

##########

test()
