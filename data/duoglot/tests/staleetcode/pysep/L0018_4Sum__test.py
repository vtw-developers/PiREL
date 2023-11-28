from L0018_4Sum import f_gold

##########
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [[1, 0, -1, 0, -2, 2], 0]
    # output: [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]
    ,
    # example 2
    [[2, 2, 2, 2, 2], 8]
    # output: [[2,2,2,2]]
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)

##########

test()
