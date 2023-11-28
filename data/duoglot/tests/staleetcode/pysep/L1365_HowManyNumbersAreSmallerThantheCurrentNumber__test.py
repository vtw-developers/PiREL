from L1365_HowManyNumbersAreSmallerThantheCurrentNumber import f_gold

##########
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [[8, 1, 2, 2, 3]]
    # output: [4,0,1,1,3]
    # EXPLANATION:   For nums[0]=8 there exist four smaller numbers than it (1, 2, 2 and 3).  For nums[1]=1 does not exist any smaller number than it. For nums[2]=2 there exist one smaller number than it (1).  For nums[3]=2 there exist one smaller number than it (1).  For nums[4]=3 there exist three smaller numbers than it (1, 2 and 2).
    ,
    # example 2
    [[6, 5, 4, 8]]
    # output: [2,1,0,3]
    ,
    # example 3
    [[7, 7, 7, 7]]
    # output: [0,0,0,0]
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)

##########

test()
