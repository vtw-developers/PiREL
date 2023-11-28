from L1035_UncrossedLines import f_gold

##########
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [[1, 4, 2], [1, 2, 4]]
    # output: 2
    # EXPLANATION:  We can draw 2 uncrossed lines as in the diagram. We cannot draw 3 uncrossed lines, because the line from nums1[1] = 4 to nums2[2] = 4 will intersect the line from nums1[2]=2 to nums2[1]=2.
    ,
    # example 2
    [[2, 5, 1, 2, 5], [10, 5, 2, 1, 5, 2]]
    # output: 3
    ,
    # example 3
    [[1, 3, 7, 1, 7, 5], [1, 9, 2, 5, 1]]
    # output: 2
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)

##########

test()
