from L0280_WiggleSort import f_gold

##########
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [[3, 5, 2, 1, 6, 4]]
    # output: [3,5,1,6,2,4]
    # EXPLANATION:  [1,6,2,5,3,4] is also accepted.
    ,
    # example 2
    [[6, 6, 5, 6, 3, 8]]
    # output: [6,6,5,6,3,8]
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)

##########

test()
