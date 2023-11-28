from L0905_SortArrayByParity import f_gold

##########
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [[3, 1, 2, 4]]
    # output: [2,4,3,1]
    # EXPLANATION:  The outputs [4,2,3,1], [2,4,1,3], and [4,2,1,3] would also be accepted.
    ,
    # example 2
    [[0]]
    # output: [0]
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)

##########

test()
