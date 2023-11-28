from L1323_Maximum69Number import f_gold

##########
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [9669]
    # output: 9969
    # EXPLANATION:   Changing the first digit results in 6669. Changing the second digit results in 9969. Changing the third digit results in 9699. Changing the fourth digit results in 9666. The maximum number is 9969.
    ,
    # example 2
    [9996]
    # output: 9999
    # EXPLANATION:  Changing the last digit 6 to 9 results in the maximum number.
    ,
    # example 3
    [9999]
    # output: 9999
    # EXPLANATION:  It is better not to apply any change.
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)

##########

test()
