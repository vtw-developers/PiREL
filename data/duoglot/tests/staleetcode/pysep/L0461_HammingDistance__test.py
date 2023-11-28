from L0461_HammingDistance import f_gold

##########
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [1, 4]
    # output: 2
    # EXPLANATION:  1   (0 0 0 1) 4   (0 1 0 0)              The above arrows point to positions where the corresponding bits are different.
    ,
    # example 2
    [3, 1]
    # output: 1
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)

##########

test()
