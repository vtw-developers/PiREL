from L0171_ExcelSheetColumnNumber import f_gold

##########
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    ["A"]
    # output: 1
    ,
    # example 2
    ["AB"]
    # output: 28
    ,
    # example 3
    ["ZY"]
    # output: 701
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)

##########

test()
