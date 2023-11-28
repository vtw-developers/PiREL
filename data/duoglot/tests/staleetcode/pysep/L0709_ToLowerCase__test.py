from L0709_ToLowerCase import f_gold

##########
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    ["Hello"]
    # output: "hello"
    ,
    # example 2
    ["here"]
    # output: "here"
    ,
    # example 3
    ["LOVELY"]
    # output: "lovely"
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)

##########

test()
