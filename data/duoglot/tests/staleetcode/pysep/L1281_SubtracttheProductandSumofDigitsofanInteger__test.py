from L1281_SubtracttheProductandSumofDigitsofanInteger import f_gold

##########
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [234]
    # output: 15
    # EXPLANATION:   Product of digits = 2 * 3 * 4 = 24  Sum of digits = 2 + 3 + 4 = 9  Result = 24 - 9 = 15
    ,
    # example 2
    [4421]
    # output: 21
    # EXPLANATION: Product of digits = 4 * 4 * 2 * 1 = 32  Sum of digits = 4 + 4 + 2 + 1 = 11  Result = 32 - 11 = 21
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)

##########

test()
