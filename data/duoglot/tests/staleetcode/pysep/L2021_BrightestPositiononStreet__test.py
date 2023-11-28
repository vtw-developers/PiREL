from L2021_BrightestPositiononStreet import f_gold

##########
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [[[-3, 2], [1, 2], [3, 3]]]
    # output: -1
    # EXPLANATION:  The first street lamp lights up the area from [(-3) - 2, (-3) + 2] = [-5, -1]. The second street lamp lights up the area from [1 - 2, 1 + 2] = [-1, 3]. The third street lamp lights up the area from [3 - 3, 3 + 3] = [0, 6].  Position -1 has a brightness of 2, illuminated by the first and second street light. Positions 0, 1, 2, and 3 have a brightness of 2, illuminated by the second and third street light. Out of all these positions, -1 is the smallest, so return it.
    ,
    # example 2
    [[[1, 0], [0, 1]]]
    # output: 1
    # EXPLANATION:  The first street lamp lights up the area from [1 - 0, 1 + 0] = [1, 1]. The second street lamp lights up the area from [0 - 1, 0 + 1] = [-1, 1].  Position 1 has a brightness of 2, illuminated by the first and second street light. Return 1 because it is the brightest position on the street.
    ,
    # example 3
    [[[1, 2]]]
    # output: -1
    # EXPLANATION:  The first street lamp lights up the area from [1 - 2, 1 + 2] = [-1, 3].  Positions -1, 0, 1, 2, and 3 have a brightness of 1, illuminated by the first street light. Out of all these positions, -1 is the smallest, so return it.
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)

##########

test()
