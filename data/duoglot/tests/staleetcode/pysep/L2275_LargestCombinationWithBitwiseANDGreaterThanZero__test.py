from L2275_LargestCombinationWithBitwiseANDGreaterThanZero import f_gold

##########
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [[16, 17, 71, 62, 12, 24, 14]]
    # output: 4
    # EXPLANATION:  The combination [16,17,62,24] has a bitwise AND of 16 & 17 & 62 & 24 = 16 > 0. The size of the combination is 4. It can be shown that no combination with a size greater than 4 has a bitwise AND greater than 0. Note that more than one combination may have the largest size. For example, the combination [62,12,24,14] has a bitwise AND of 62 & 12 & 24 & 14 = 8 > 0.
    ,
    # example 2
    [[8, 8]]
    # output: 2
    # EXPLANATION:  The largest combination [8,8] has a bitwise AND of 8 & 8 = 8 > 0. The size of the combination is 2, so we return 2.
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)

##########

test()
