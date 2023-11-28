from L2094_Finding3DigitEvenNumbers import f_gold

##########
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [[2, 1, 3, 0]]
    # output: [102,120,130,132,210,230,302,310,312,320]
    # EXPLANATION:  All the possible integers that follow the requirements are in the output array.  Notice that there are no <strong>odd</strong> integers or integers with <strong>leading zeros</strong>.
    ,
    # example 2
    [[2, 2, 8, 8, 2]]
    # output: [222,228,282,288,822,828,882]
    # EXPLANATION:  The same digit can be used as many times as it appears in digits.  In this example, the digit 8 is used twice each time in 288, 828, and 882.
    ,
    # example 3
    [[3, 7, 5]]
    # output: []
    # EXPLANATION:  No <strong>even</strong> integers can be formed using the given digits.
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)

##########

test()
