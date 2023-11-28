from L0249_GroupShiftedStrings import f_gold

##########
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [["abc", "bcd", "acef", "xyz", "az", "ba", "a", "z"]]
    # output: [["acef"],["a","z"],["abc","bcd","xyz"],["az","ba"]]
    ,
    # example 2
    [["a"]]
    # output: [["a"]]
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)

##########

test()
