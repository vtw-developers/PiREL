from L0357_CountNumberswithUniqueDigits import f_gold

##########
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [2]
    # output: 91
    # EXPLANATION:  The answer should be the total numbers in the range of 0   x < 100, excluding 11,22,33,44,55,66,77,88,99
    ,
    # example 2
    [0]
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
