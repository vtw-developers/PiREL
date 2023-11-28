from L0959_RegionsCutBySlashes import f_gold

##########
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [[" /", "/ "]]
    # output: 2
    ,
    # example 2
    [[" /", "  "]]
    # output: 1
    ,
    # example 3
    [["/\\", "\\/"]]
    # output: 5
    # EXPLANATION: Recall that because \ characters are escaped, "\\/" refers to \/, and "/\\" refers to /\.
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)

##########

test()
