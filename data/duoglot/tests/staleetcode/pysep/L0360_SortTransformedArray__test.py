from L0360_SortTransformedArray import f_gold

##########
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [[-4, -2, 2, 4], 1, 3, 5]
    # output: [3,9,15,33]
    ,
    # example 2
    [[-4, -2, 2, 4], -1, 3, 5]
    # output: [-23,-5,1,7]
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)

##########

test()
