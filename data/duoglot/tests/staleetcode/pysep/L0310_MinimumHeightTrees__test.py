from L0310_MinimumHeightTrees import f_gold

##########
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [4, [[1, 0], [1, 2], [1, 3]]]
    # output: [1]
    # EXPLANATION:  As shown, the height of the tree is 1 when the root is the node with label 1 which is the only MHT.
    ,
    # example 2
    [6, [[3, 0], [3, 1], [3, 2], [3, 4], [5, 4]]]
    # output: [3,4]
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)

##########

test()
