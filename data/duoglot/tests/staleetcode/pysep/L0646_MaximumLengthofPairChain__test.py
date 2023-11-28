from L0646_MaximumLengthofPairChain import f_gold

##########
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [[[1, 2], [2, 3], [3, 4]]]
    # output: 2
    # EXPLANATION:  The longest chain is [1,2] -> [3,4].
    ,
    # example 2
    [[[1, 2], [7, 8], [4, 5]]]
    # output: 3
    # EXPLANATION:  The longest chain is [1,2] -> [4,5] -> [7,8].
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)

##########

test()
