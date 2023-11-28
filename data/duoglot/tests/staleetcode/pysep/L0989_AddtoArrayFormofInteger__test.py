from L0989_AddtoArrayFormofInteger import f_gold

##########
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [[1, 2, 0, 0], 34]
    # output: [1,2,3,4]
    # EXPLANATION:  1200 + 34 = 1234
    ,
    # example 2
    [[2, 7, 4], 181]
    # output: [4,5,5]
    # EXPLANATION:  274 + 181 = 455
    ,
    # example 3
    [[2, 1, 5], 806]
    # output: [1,0,2,1]
    # EXPLANATION:  215 + 806 = 1021
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)

##########

test()
