from L0258_AddDigits import f_gold

##########
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [38]
    # output: 2
    # EXPLANATION:  The process is 38 --> 3 + 8 --> 11 11 --> 1 + 1 --> 2  Since 2 has only one digit, return it.
    ,
    # example 2
    [0]
    # output: 0
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)

##########

test()
