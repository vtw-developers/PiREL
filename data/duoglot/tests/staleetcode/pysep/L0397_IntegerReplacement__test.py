from L0397_IntegerReplacement import f_gold

##########
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [8]
    # output: 3
    # EXPLANATION:  8 -> 4 -> 2 -> 1
    ,
    # example 2
    [7]
    # output: 4
    # EXPLANATION: 7 -> 8 -> 4 -> 2 -> 1 or 7 -> 6 -> 3 -> 2 -> 1
    ,
    # example 3
    [4]
    # output: 2
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)

##########

test()
