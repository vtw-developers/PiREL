from L0961_NRepeatedElementinSize2NArray import f_gold

##########
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [[1, 2, 3, 3]]
    # output: 3
    ,
    # example 2
    [[2, 1, 2, 5, 3, 2]]
    # output: 2
    ,
    # example 3
    [[5, 1, 5, 2, 5, 3, 5, 4]]
    # output: 5
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)

##########

test()
