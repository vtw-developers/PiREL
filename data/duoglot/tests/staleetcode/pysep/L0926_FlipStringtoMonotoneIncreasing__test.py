from L0926_FlipStringtoMonotoneIncreasing import f_gold

##########
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    ["00110"]
    # output: 1
    # EXPLANATION:  We flip the last digit to get 00111.
    ,
    # example 2
    ["010110"]
    # output: 2
    # EXPLANATION:  We flip to get 011111, or alternatively 000111.
    ,
    # example 3
    ["00011000"]
    # output: 2
    # EXPLANATION:  We flip to get 00000000.
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)

##########

test()
