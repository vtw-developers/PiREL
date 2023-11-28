from L1827_MinimumOperationstoMaketheArrayIncreasing import f_gold

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
    # output: 3
    # EXPLANATION:  You can do the following operations:  1) Increment nums[2], so nums becomes [1,1,<u><strong>2</strong></u>].  2) Increment nums[1], so nums becomes [1,<u><strong>2</strong></u>,2].  3) Increment nums[2], so nums becomes [1,2,<u><strong>3</strong></u>].
    ,
    # example 2
    [[1, 5, 2, 4, 1]]
    # output: 14
    ,
    # example 3
    [[8]]
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
