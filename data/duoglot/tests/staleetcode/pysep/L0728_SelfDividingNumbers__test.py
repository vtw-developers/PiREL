from L0728_SelfDividingNumbers import f_gold

##########
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [1, 22]
    # output: [1,2,3,4,5,6,7,8,9,11,12,15,22]
    ,
    # example 2
    [47, 85]
    # output: [48,55,66,77]
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)

##########

test()
