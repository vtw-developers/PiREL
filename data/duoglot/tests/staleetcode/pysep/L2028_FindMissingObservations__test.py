from L2028_FindMissingObservations import f_gold

##########
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [[3, 2, 4, 3], 4, 2]
    # output: [6,6]
    # EXPLANATION:  The mean of all n + m rolls is (3 + 2 + 4 + 3 + 6 + 6) / 6 = 4.
    ,
    # example 2
    [[1, 5, 6], 3, 4]
    # output: [2,3,2,2]
    # EXPLANATION:  The mean of all n + m rolls is (1 + 5 + 6 + 2 + 3 + 2 + 2) / 7 = 3.
    ,
    # example 3
    [[1, 2, 3, 4], 6, 4]
    # output: []
    # EXPLANATION:  It is impossible for the mean to be 6 no matter what the 4 missing rolls are.
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)

##########

test()
