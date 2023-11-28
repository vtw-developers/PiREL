from L1442_CountTripletsThatCanFormTwoArraysofEqualXOR import f_gold

##########
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [[2, 3, 1, 6, 7]]
    # output: 4
    # EXPLANATION:  The triplets are (0,1,2), (0,2,2), (2,3,4) and (2,4,4)
    ,
    # example 2
    [[1, 1, 1, 1, 1]]
    # output: 10
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)

##########

test()
