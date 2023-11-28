from L1512_NumberofGoodPairs import f_gold

##########
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [[1, 2, 3, 1, 1, 3]]
    # output: 4
    # EXPLANATION:  There are 4 good pairs (0,3), (0,4), (3,4), (2,5) 0-indexed.
    ,
    # example 2
    [[1, 1, 1, 1]]
    # output: 6
    # EXPLANATION:  Each pair in the array are <em>good</em>.
    ,
    # example 3
    [[1, 2, 3]]
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
