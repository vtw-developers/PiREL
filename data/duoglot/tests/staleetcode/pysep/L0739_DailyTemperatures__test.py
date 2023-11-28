from L0739_DailyTemperatures import f_gold

##########
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [[73, 74, 75, 71, 69, 72, 76, 73]]
    # output: [1,1,4,2,1,1,0,0]
    ,
    # example 2
    [[30, 40, 50, 60]]
    # output: [1,1,1,0]
    ,
    # example 3
    [[30, 60, 90]]
    # output: [1,1,0]
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)

##########

test()
