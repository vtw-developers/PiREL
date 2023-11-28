from L1719_NumberOfWaysToReconstructATree import f_gold

##########
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [[[1, 2], [2, 3]]]
    # output: 1
    # EXPLANATION:  There is exactly one valid rooted tree, which is shown in the above figure.
    ,
    # example 2
    [[[1, 2], [2, 3], [1, 3]]]
    # output: 2
    # EXPLANATION:  There are multiple valid rooted trees. Three of them are shown in the above figures.
    ,
    # example 3
    [[[1, 2], [2, 3], [2, 4], [1, 5]]]
    # output: 0
    # EXPLANATION:  There are no valid rooted trees.
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)

##########

test()
