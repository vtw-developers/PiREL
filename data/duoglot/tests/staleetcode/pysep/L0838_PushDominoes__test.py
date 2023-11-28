from L0838_PushDominoes import f_gold

##########
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    ["RR.L"]
    # output: "RR.L"
    # EXPLANATION:  The first domino expends no additional force on the second domino.
    ,
    # example 2
    [".L.R...LR..L.."]
    # output: "LL.RR.LLRRLL.."
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)

##########

test()
