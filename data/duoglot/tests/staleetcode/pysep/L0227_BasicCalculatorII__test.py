from L0227_BasicCalculatorII import f_gold

##########
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    ["3+2*2"]
    # output: 7
    ,
    # example 2
    [" 3/2 "]
    # output: 1
    ,
    # example 3
    [" 3+5 / 2 "]
    # output: 5
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)

##########

test()
