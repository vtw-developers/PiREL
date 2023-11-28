from L0259_3SumSmaller import f_gold

##########
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [[-2, 0, 1, 3], 2]
    # output: 2
    # EXPLANATION:  Because there are two triplets which sums are less than 2: [-2,0,1] [-2,0,3]
    ,
    # example 2
    [[], 0]
    # output: 0
    ,
    # example 3
    [[0], 0]
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
