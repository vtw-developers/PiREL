from L1122_RelativeSortArray import f_gold

##########
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [[2, 3, 1, 3, 2, 4, 6, 7, 9, 2, 19], [2, 1, 4, 3, 9, 6]]
    # output: [2,2,2,1,4,3,3,9,6,7,19]
    ,
    # example 2
    [[28, 6, 22, 8, 44, 17], [22, 28, 8, 6]]
    # output: [22,28,8,6,17,44]
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)

##########

test()
