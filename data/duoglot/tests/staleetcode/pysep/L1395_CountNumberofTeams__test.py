from L1395_CountNumberofTeams import f_gold

##########
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [[2, 5, 3, 4, 1]]
    # output: 3
    # EXPLANATION:  We can form three teams given the conditions. (2,3,4), (5,4,1), (5,3,1).
    ,
    # example 2
    [[2, 1, 3]]
    # output: 0
    # EXPLANATION:  We can't form any team given the conditions.
    ,
    # example 3
    [[1, 2, 3, 4]]
    # output: 4
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)

##########

test()
