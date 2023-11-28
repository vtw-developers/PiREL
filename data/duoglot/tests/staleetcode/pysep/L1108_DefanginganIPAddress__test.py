from L1108_DefanginganIPAddress import f_gold

##########
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    ["1.1.1.1"]
    # output: "1[.]1[.]1[.]1"
    ,
    # example 2
    ["255.100.50.0"]
    # output: "255[.]100[.]50[.]0"
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)

##########

test()
