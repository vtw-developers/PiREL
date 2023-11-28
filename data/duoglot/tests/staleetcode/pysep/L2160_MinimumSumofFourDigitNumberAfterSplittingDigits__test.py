from L2160_MinimumSumofFourDigitNumberAfterSplittingDigits import f_gold

##########
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [2932]
    # output: 52
    # EXPLANATION:  Some possible pairs [new1, new2] are [29, 23], [223, 9], etc. The minimum sum can be obtained by the pair [29, 23]: 29 + 23 = 52.
    ,
    # example 2
    [4009]
    # output: 13
    # EXPLANATION:  Some possible pairs [new1, new2] are [0, 49], [490, 0], etc.  The minimum sum can be obtained by the pair [4, 9]: 4 + 9 = 13.
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)

##########

test()
