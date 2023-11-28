from L1943_DescribethePainting import f_gold

##########
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [[[1, 4, 5], [4, 7, 7], [1, 7, 9]]]
    # output: [[1,4,14],[4,7,16]]
    # EXPLANATION: The painting can be described as follows: - [1,4) is colored {5,9} (with a sum of 14) from the first and third segments. - [4,7) is colored {7,9} (with a sum of 16) from the second and third segments.
    ,
    # example 2
    [[[1, 7, 9], [6, 8, 15], [8, 10, 7]]]
    # output: [[1,6,9],[6,7,24],[7,8,15],[8,10,7]]
    # EXPLANATION: The painting can be described as follows: - [1,6) is colored 9 from the first segment. - [6,7) is colored {9,15} (with a sum of 24) from the first and second segments. - [7,8) is colored 15 from the second segment. - [8,10) is colored 7 from the third segment.
    ,
    # example 3
    [[[1, 4, 5], [1, 4, 7], [4, 7, 1], [4, 7, 11]]]
    # output: [[1,4,12],[4,7,12]]
    # EXPLANATION: The painting can be described as follows: - [1,4) is colored {5,7} (with a sum of 12) from the first and second segments. - [4,7) is colored {1,11} (with a sum of 12) from the third and fourth segments. Note that returning a single segment [1,7) is incorrect because the mixed color sets are different.
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)

##########

test()
