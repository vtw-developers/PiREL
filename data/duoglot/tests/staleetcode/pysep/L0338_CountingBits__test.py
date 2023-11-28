from L0338_CountingBits import f_gold

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
    # output: [0,1,1]
    # EXPLANATION:  0 --> 0 1 --> 1 2 --> 10
    ,
    # example 2
    [5]
    # output: [0,1,1,2,1,2]
    # EXPLANATION:  0 --> 0 1 --> 1 2 --> 10 3 --> 11 4 --> 100 5 --> 101
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)

##########

test()
