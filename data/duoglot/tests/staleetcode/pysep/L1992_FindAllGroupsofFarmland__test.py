from L1992_FindAllGroupsofFarmland import f_gold

##########
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [[[1, 0, 0], [0, 1, 1], [0, 1, 1]]]
    # output: [[0,0,0,0],[1,1,2,2]]
    # EXPLANATION:  The first group has a top left corner at land[0][0] and a bottom right corner at land[0][0]. The second group has a top left corner at land[1][1] and a bottom right corner at land[2][2].
    ,
    # example 2
    [[[1, 1], [1, 1]]]
    # output: [[0,0,1,1]]
    # EXPLANATION:  The first group has a top left corner at land[0][0] and a bottom right corner at land[1][1].
    ,
    # example 3
    [[[0]]]
    # output: []
    # EXPLANATION:  There are no groups of farmland.
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)

##########

test()
