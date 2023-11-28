from L0458_PoorPigs import f_gold

##########
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [1000, 15, 60]
    # output: 5
    ,
    # example 2
    [4, 15, 15]
    # output: 2
    ,
    # example 3
    [4, 15, 30]
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
