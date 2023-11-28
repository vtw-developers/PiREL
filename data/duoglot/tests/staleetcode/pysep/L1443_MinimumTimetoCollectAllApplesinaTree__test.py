from L1443_MinimumTimetoCollectAllApplesinaTree import f_gold

##########
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [7, [[0, 1], [0, 2], [1, 4], [1, 5], [2, 3], [2, 6]], [False, False, True, False, True, True, False]]
    # output: 8
    # EXPLANATION:  The figure above represents the given tree where red vertices have an apple. One optimal path to collect all apples is shown by the green arrows.
    ,
    # example 2
    [7, [[0, 1], [0, 2], [1, 4], [1, 5], [2, 3], [2, 6]], [False, False, True, False, False, True, False]]
    # output: 6
    # EXPLANATION:  The figure above represents the given tree where red vertices have an apple. One optimal path to collect all apples is shown by the green arrows.
    ,
    # example 3
    [7, [[0, 1], [0, 2], [1, 4], [1, 5], [2, 3], [2, 6]], [False, False, False, False, False, False, False]]
    # output: 0
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)

##########

test()
