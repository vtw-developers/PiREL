from L0335_SelfCrossing import f_gold

##########
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [[2, 1, 1, 2]]
    # output: true
    ,
    # example 2
    [[1, 2, 3, 4]]
    # output: false
    ,
    # example 3
    [[1, 1, 1, 1]]
    # output: true
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)

##########

test()
