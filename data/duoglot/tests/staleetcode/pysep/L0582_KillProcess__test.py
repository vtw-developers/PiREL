from L0582_KillProcess import f_gold

##########
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [[1, 3, 10, 5], [3, 0, 5, 3], 5]
    # output: [5,10]
    # EXPLANATION:  The processes colored in red are the processes that should be killed.
    ,
    # example 2
    [[1], [0], 1]
    # output: [1]
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)

##########

test()
