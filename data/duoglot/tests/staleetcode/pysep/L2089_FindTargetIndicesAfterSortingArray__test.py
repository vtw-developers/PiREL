from L2089_FindTargetIndicesAfterSortingArray import f_gold

##########
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [[1, 2, 5, 2, 3], 2]
    # output: [1,2]
    # EXPLANATION:  After sorting, nums is [1,<u><strong>2</strong></u>,<u><strong>2</strong></u>,3,5]. The indices where nums[i] == 2 are 1 and 2.
    ,
    # example 2
    [[1, 2, 5, 2, 3], 3]
    # output: [3]
    # EXPLANATION:  After sorting, nums is [1,2,2,<u><strong>3</strong></u>,5]. The index where nums[i] == 3 is 3.
    ,
    # example 3
    [[1, 2, 5, 2, 3], 5]
    # output: [4]
    # EXPLANATION:  After sorting, nums is [1,2,2,3,<u><strong>5</strong></u>]. The index where nums[i] == 5 is 4.
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)

##########

test()
