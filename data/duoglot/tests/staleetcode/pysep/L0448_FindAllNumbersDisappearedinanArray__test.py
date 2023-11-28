from L0448_FindAllNumbersDisappearedinanArray import f_gold

##########
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [[4, 3, 2, 7, 8, 2, 3, 1]]
    # output: [5,6]
    ,
    # example 2
    [[1, 1]]
    # output: [2]
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)

##########

test()
