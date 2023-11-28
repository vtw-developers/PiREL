from L0165_CompareVersionNumbers import f_gold

##########
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    ["1.01", "1.001"]
    # output: 0
    # EXPLANATION:  Ignoring leading zeroes, both "01" and "001" represent the same integer "1".
    ,
    # example 2
    ["1.0", "1.0.0"]
    # output: 0
    # EXPLANATION:  version1 does not specify revision 2, which means it is treated as "0".
    ,
    # example 3
    ["0.1", "1.1"]
    # output: -1
    # EXPLANATION:  version1's revision 0 is "0", while version2's revision 0 is "1". 0 < 1, so version1 < version2.
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)

##########

test()
