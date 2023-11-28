from L1283_FindtheSmallestDivisorGivenaThreshold import f_gold

##########
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [[1, 2, 5, 9], 6]
    # output: 5
    # EXPLANATION:  We can get a sum to 17 (1+2+5+9) if the divisor is 1.  If the divisor is 4 we can get a sum of 7 (1+1+2+3) and if the divisor is 5 the sum will be 5 (1+1+1+2).
    ,
    # example 2
    [[44, 22, 33, 11, 1], 5]
    # output: 44
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)

##########

test()
