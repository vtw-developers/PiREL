from L1848_MinimumDistancetotheTargetElement import f_gold

##########
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [[1, 2, 3, 4, 5], 5, 3]
    # output: 1
    # EXPLANATION:  nums[4] = 5 is the only value equal to target, so the answer is abs(4 - 3) = 1.
    ,
    # example 2
    [[1], 1, 0]
    # output: 0
    # EXPLANATION:  nums[0] = 1 is the only value equal to target, so the answer is abs(0 - 0) = 0.
    ,
    # example 3
    [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1], 1, 0]
    # output: 0
    # EXPLANATION:  Every value of nums is 1, but nums[0] minimizes abs(i - start), which is abs(0 - 0) = 0.
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)

##########

test()
