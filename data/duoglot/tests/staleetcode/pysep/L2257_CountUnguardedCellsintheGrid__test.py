from L2257_CountUnguardedCellsintheGrid import f_gold

##########
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [4, 6, [[0, 0], [1, 1], [2, 3]], [[0, 1], [2, 2], [1, 4]]]
    # output: 7
    # EXPLANATION:  The guarded and unguarded cells are shown in red and green respectively in the above diagram. There are a total of 7 unguarded cells, so we return 7.
    ,
    # example 2
    [3, 3, [[1, 1]], [[0, 1], [1, 0], [2, 1], [1, 2]]]
    # output: 4
    # EXPLANATION:  The unguarded cells are shown in green in the above diagram. There are a total of 4 unguarded cells, so we return 4.
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)

##########

test()
