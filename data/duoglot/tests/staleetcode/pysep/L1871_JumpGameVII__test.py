from L1871_JumpGameVII import f_gold

##########
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    ["011010", 2, 3]
    # output: true
    # EXPLANATION:  In the first step, move from index 0 to index 3.  In the second step, move from index 3 to index 5.
    ,
    # example 2
    ["01101110", 2, 3]
    # output: false
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)

##########

test()
