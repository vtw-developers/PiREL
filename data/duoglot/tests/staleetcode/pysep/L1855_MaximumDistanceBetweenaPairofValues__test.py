from L1855_MaximumDistanceBetweenaPairofValues import f_gold

##########
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [[55, 30, 5, 4, 2], [100, 20, 10, 10, 5]]
    # output: 2
    # EXPLANATION:  The valid pairs are (0,0), (2,2), (2,3), (2,4), (3,3), (3,4), and (4,4). The maximum distance is 2 with pair (2,4).
    ,
    # example 2
    [[2, 2, 2], [10, 10, 1]]
    # output: 1
    # EXPLANATION:  The valid pairs are (0,0), (0,1), and (1,1). The maximum distance is 1 with pair (0,1).
    ,
    # example 3
    [[30, 29, 19, 5], [25, 25, 25, 25, 25]]
    # output: 2
    # EXPLANATION:  The valid pairs are (2,2), (2,3), (2,4), (3,3), and (3,4). The maximum distance is 2 with pair (2,4).
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)

##########

test()
