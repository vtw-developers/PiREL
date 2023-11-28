from L1295_FindNumberswithEvenNumberofDigits import f_gold

##########
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [[12, 345, 2, 6, 7896]]
    # output: 2
    # EXPLANATION: 12 contains 2 digits (even number of digits).  345 contains 3 digits (odd number of digits).  2 contains 1 digit (odd number of digits).  6 contains 1 digit (odd number of digits).  7896 contains 4 digits (even number of digits).  Therefore only 12 and 7896 contain an even number of digits.
    ,
    # example 2
    [[555, 901, 482, 1771]]
    # output: 1
    # EXPLANATION:  Only 1771 contains an even number of digits.
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)

##########

test()
