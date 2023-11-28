from L1118_NumberofDaysinaMonth import f_gold

##########
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [1992, 7]
    # output: 31
    ,
    # example 2
    [2000, 2]
    # output: 29
    ,
    # example 3
    [1900, 2]
    # output: 28
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)

##########

test()
