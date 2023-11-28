from L0492_ConstructtheRectangle import f_gold

##########
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [4]
    # output: [2,2]
    # EXPLANATION:  The target area is 4, and all the possible ways to construct it are [1,4], [2,2], [4,1].  But according to requirement 2, [1,4] is illegal; according to requirement 3,  [4,1] is not optimal compared to [2,2]. So the length L is 2, and the width W is 2.
    ,
    # example 2
    [37]
    # output: [37,1]
    ,
    # example 3
    [122122]
    # output: [427,286]
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)

##########

test()
