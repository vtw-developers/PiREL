from L0006_ZigzagConversion import f_gold

##########
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    ["PAYPALISHIRING", 3]
    # output: "PAHNAPLSIIGYIR"
    ,
    # example 2
    ["PAYPALISHIRING", 4]
    # output: "PINALSIGYAHRPI"
    # EXPLANATION:  P     I    N A   L S  I G Y A   H R P     I
    ,
    # example 3
    ["A", 1]
    # output: "A"
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)

##########

test()
