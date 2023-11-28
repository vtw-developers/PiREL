from L0447_NumberofBoomerangs import f_gold

##########
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [[[0, 0], [1, 0], [2, 0]]]
    # output: 2
    # EXPLANATION:  The two boomerangs are [[1,0],[0,0],[2,0]] and [[1,0],[2,0],[0,0]].
    ,
    # example 2
    [[[1, 1], [2, 2], [3, 3]]]
    # output: 2
    ,
    # example 3
    [[[1, 1]]]
    # output: 0
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)

##########

test()
