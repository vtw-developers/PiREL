from L0524_LongestWordinDictionarythroughDeleting import f_gold

##########
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    ["abpcplea", ["ale", "apple", "monkey", "plea"]]
    # output: "apple"
    ,
    # example 2
    ["abpcplea", ["a", "b", "c"]]
    # output: "a"
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)

##########

test()
