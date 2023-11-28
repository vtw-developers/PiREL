from L1480_RunningSumof1dArray import f_gold

##########
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [[1, 2, 3, 4]]
    # output: [1,3,6,10]
    # EXPLANATION:  Running sum is obtained as follows: [1, 1+2, 1+2+3, 1+2+3+4].
    ,
    # example 2
    [[1, 1, 1, 1, 1]]
    # output: [1,2,3,4,5]
    # EXPLANATION:  Running sum is obtained as follows: [1, 1+1, 1+1+1, 1+1+1+1, 1+1+1+1+1].
    ,
    # example 3
    [[3, 1, 2, 10, 1]]
    # output: [3,4,6,16,17]
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)

##########

test()
