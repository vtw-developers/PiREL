from L2239_FindClosestNumbertoZero import f_gold

##########
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [[-4, -2, 1, 4, 8]]
    # output: 1
    # EXPLANATION:  The distance from -4 to 0 is |-4| = 4. The distance from -2 to 0 is |-2| = 2. The distance from 1 to 0 is |1| = 1. The distance from 4 to 0 is |4| = 4. The distance from 8 to 0 is |8| = 8. Thus, the closest number to 0 in the array is 1.
    ,
    # example 2
    [[2, -1, 1]]
    # output: 1
    # EXPLANATION:  1 and -1 are both the closest numbers to 0, so 1 being larger is returned.
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)

##########

test()
