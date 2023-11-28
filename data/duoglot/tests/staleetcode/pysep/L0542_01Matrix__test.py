from L0542_01Matrix import f_gold

##########
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [[[0, 0, 0], [0, 1, 0], [0, 0, 0]]]
    # output: [[0,0,0],[0,1,0],[0,0,0]]
    ,
    # example 2
    [[[0, 0, 0], [0, 1, 0], [1, 1, 1]]]
    # output: [[0,0,0],[0,1,0],[1,2,1]]
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)

##########

test()
