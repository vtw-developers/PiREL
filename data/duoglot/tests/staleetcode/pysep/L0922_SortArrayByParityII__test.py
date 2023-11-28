from L0922_SortArrayByParityII import f_gold

##########
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [[4, 2, 5, 7]]
    # output: [4,5,2,7]
    # EXPLANATION:  [4,7,2,5], [2,5,4,7], [2,7,4,5] would also have been accepted.
    ,
    # example 2
    [[2, 3]]
    # output: [2,3]
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)

##########

test()
