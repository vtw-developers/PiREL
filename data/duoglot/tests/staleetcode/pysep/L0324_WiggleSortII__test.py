from L0324_WiggleSortII import f_gold

##########
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [[1, 5, 1, 1, 6, 4]]
    # output: [1,6,1,5,1,4]
    # EXPLANATION:  [1,4,1,5,1,6] is also accepted.
    ,
    # example 2
    [[1, 3, 2, 2, 3, 1]]
    # output: [2,3,1,3,1,2]
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)

##########

test()
