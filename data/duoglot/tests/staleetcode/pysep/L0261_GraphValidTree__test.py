from L0261_GraphValidTree import f_gold

##########
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [5, [[0, 1], [0, 2], [0, 3], [1, 4]]]
    # output: true
    ,
    # example 2
    [5, [[0, 1], [1, 2], [2, 3], [1, 3], [1, 4]]]
    # output: false
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)

##########

test()
