from L0415_AddStrings import f_gold

##########
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    ["11", "123"]
    # output: "134"
    ,
    # example 2
    ["456", "77"]
    # output: "533"
    ,
    # example 3
    ["0", "0"]
    # output: "0"
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)

##########

test()
