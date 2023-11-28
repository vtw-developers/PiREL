from L0039_CombinationSum import f_gold

##########
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [[2, 3, 6, 7], 7]
    # output: [[2,2,3],[7]]
    # EXPLANATION:  2 and 3 are candidates, and 2 + 2 + 3 = 7. Note that 2 can be used multiple times. 7 is a candidate, and 7 = 7. These are the only two combinations.
    ,
    # example 2
    [[2, 3, 5], 8]
    # output: [[2,2,2,2],[2,3,3],[3,5]]
    ,
    # example 3
    [[2], 1]
    # output: []
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)

##########

test()
