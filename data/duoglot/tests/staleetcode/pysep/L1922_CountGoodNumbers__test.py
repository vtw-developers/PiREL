from L1922_CountGoodNumbers import f_gold

##########
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [1]
    # output: 5
    # EXPLANATION:  The good numbers of length 1 are "0", "2", "4", "6", "8".
    ,
    # example 2
    [4]
    # output: 400
    ,
    # example 3
    [50]
    # output: 564908303
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)

##########

test()
