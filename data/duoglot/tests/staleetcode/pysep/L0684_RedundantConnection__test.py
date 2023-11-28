from L0684_RedundantConnection import f_gold

##########
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [[[1, 2], [1, 3], [2, 3]]]
    # output: [2,3]
    ,
    # example 2
    [[[1, 2], [2, 3], [3, 4], [1, 4], [1, 5]]]
    # output: [1,4]
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)

##########

test()
