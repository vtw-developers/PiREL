from L0816_AmbiguousCoordinates import f_gold

##########
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    ["(123)"]
    # output: ["(1, 2.3)","(1, 23)","(1.2, 3)","(12, 3)"]
    ,
    # example 2
    ["(0123)"]
    # output: ["(0, 1.23)","(0, 12.3)","(0, 123)","(0.1, 2.3)","(0.1, 23)","(0.12, 3)"]
    # EXPLANATION:  0.0, 00, 0001 or 00.01 are not allowed.
    ,
    # example 3
    ["(00011)"]
    # output: ["(0, 0.011)","(0.001, 1)"]
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)

##########

test()
