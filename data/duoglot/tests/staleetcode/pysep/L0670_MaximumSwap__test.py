from L0670_MaximumSwap import f_gold

##########
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [2736]
    # output: 7236
    # EXPLANATION:  Swap the number 2 and the number 7.
    ,
    # example 2
    [9973]
    # output: 9973
    # EXPLANATION:  No swap.
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)

##########

test()
