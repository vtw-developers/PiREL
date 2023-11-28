from L1245_TreeDiameter import f_gold

##########
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [[[0, 1], [0, 2]]]
    # output: 2
    # EXPLANATION:  The longest path of the tree is the path 1 - 0 - 2.
    ,
    # example 2
    [[[0, 1], [1, 2], [2, 3], [1, 4], [4, 5]]]
    # output: 4
    # EXPLANATION:  The longest path of the tree is the path 3 - 2 - 1 - 4 - 5.
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)

##########

test()
