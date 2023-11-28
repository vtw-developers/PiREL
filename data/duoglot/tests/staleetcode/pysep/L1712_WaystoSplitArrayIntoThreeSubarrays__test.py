from L1712_WaystoSplitArrayIntoThreeSubarrays import f_gold

##########
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [[1, 1, 1]]
    # output: 1
    # EXPLANATION:  The only good way to split nums is [1] [1] [1].
    ,
    # example 2
    [[1, 2, 2, 2, 5, 0]]
    # output: 3
    # EXPLANATION:  There are three good ways of splitting nums:  [1] [2] [2,2,5,0]  [1] [2,2] [2,5,0]  [1,2] [2,2] [5,0]
    ,
    # example 3
    [[3, 2, 1]]
    # output: 0
    # EXPLANATION:  There is no good way to split nums.
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)

##########

test()
