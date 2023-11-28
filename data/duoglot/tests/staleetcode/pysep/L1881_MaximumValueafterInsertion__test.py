from L1881_MaximumValueafterInsertion import f_gold

##########
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    ["99", 9]
    # output: "999"
    # EXPLANATION:  The result is the same regardless of where you insert 9.
    ,
    # example 2
    ["-13", 2]
    # output: "-123"
    # EXPLANATION:  You can make n one of {-213, -123, -132}, and the largest of those three is -123.
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)

##########

test()
