from L0015_3Sum import f_gold

##########
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [[-1, 0, 1, 2, -1, -4]]
    # output: [[-1,-1,2],[-1,0,1]]
    ,
    # example 2
    [[]]
    # output: []
    ,
    # example 3
    [[0]]
    # output: []
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)

##########

test()
