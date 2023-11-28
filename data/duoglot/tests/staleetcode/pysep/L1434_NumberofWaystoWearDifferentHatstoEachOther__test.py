from L1434_NumberofWaystoWearDifferentHatstoEachOther import f_gold

##########
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [[[3, 4], [4, 5], [5]]]
    # output: 1
    # EXPLANATION:  There is only one way to choose hats given the conditions.  First person choose hat 3, Second person choose hat 4 and last one hat 5.
    ,
    # example 2
    [[[3, 5, 1], [3, 5]]]
    # output: 4
    # EXPLANATION:  There are 4 ways to choose hats: (3,5), (5,3), (1,3) and (1,5)
    ,
    # example 3
    [[[1, 2, 3, 4], [1, 2, 3, 4], [1, 2, 3, 4], [1, 2, 3, 4]]]
    # output: 24
    # EXPLANATION:  Each person can choose hats labeled from 1 to 4. Number of Permutations of (1,2,3,4) = 24.
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)

##########

test()
