from L0689_MaximumSumof3NonOverlappingSubarrays import f_gold

##########
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [[1, 2, 1, 2, 6, 7, 5, 1], 2]
    # output: [0,3,5]
    # EXPLANATION:  Subarrays [1, 2], [2, 6], [7, 5] correspond to the starting indices [0, 3, 5]. We could have also taken [2, 1], but an answer of [1, 3, 5] would be lexicographically larger.
    ,
    # example 2
    [[1, 2, 1, 2, 1, 2, 1, 2, 1], 2]
    # output: [0,2,4]
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)

##########

test()
