from L1007_MinimumDominoRotationsForEqualRow import f_gold

##########
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [[2, 1, 2, 4, 2, 2], [5, 2, 6, 2, 3, 2]]
    # output: 2
    # EXPLANATION:   The first figure represents the dominoes as given by tops and bottoms: before we do any rotations. If we rotate the second and fourth dominoes, we can make every value in the top row equal to 2, as indicated by the second figure.
    ,
    # example 2
    [[3, 5, 1, 2, 3], [3, 6, 3, 3, 4]]
    # output: -1
    # EXPLANATION:   In this case, it is not possible to rotate the dominoes to make one row of values equal.
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)

##########

test()
