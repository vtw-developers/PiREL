from L1342_NumberofStepstoReduceaNumbertoZero import f_gold

##########
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [14]
    # output: 6
    # EXPLANATION:   Step 1) 14 is even; divide by 2 and obtain 7.  Step 2) 7 is odd; subtract 1 and obtain 6. Step 3) 6 is even; divide by 2 and obtain 3.  Step 4) 3 is odd; subtract 1 and obtain 2.  Step 5) 2 is even; divide by 2 and obtain 1.  Step 6) 1 is odd; subtract 1 and obtain 0.
    ,
    # example 2
    [8]
    # output: 4
    # EXPLANATION:   Step 1) 8 is even; divide by 2 and obtain 4.  Step 2) 4 is even; divide by 2 and obtain 2.  Step 3) 2 is even; divide by 2 and obtain 1.  Step 4) 1 is odd; subtract 1 and obtain 0.
    ,
    # example 3
    [123]
    # output: 12
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)

##########

test()
