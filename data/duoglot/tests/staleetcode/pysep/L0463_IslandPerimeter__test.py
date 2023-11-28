from L0463_IslandPerimeter import f_gold

##########
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [[[0, 1, 0, 0], [1, 1, 1, 0], [0, 1, 0, 0], [1, 1, 0, 0]]]
    # output: 16
    # EXPLANATION:  The perimeter is the 16 yellow stripes in the image above.
    ,
    # example 2
    [[[1]]]
    # output: 4
    ,
    # example 3
    [[[1, 0]]]
    # output: 4
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)

##########

test()
