from L0356_LineReflection import f_gold

##########
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [[[1, 1], [-1, 1]]]
    # output: true
    # EXPLANATION:  We can choose the line x = 0.
    ,
    # example 2
    [[[1, 1], [-1, -1]]]
    # output: false
    # EXPLANATION:  We can't choose a line.
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)

##########

test()
