from L2279_MaximumBagsWithFullCapacityofRocks import f_gold

##########
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [[2, 3, 4, 5], [1, 2, 4, 4], 2]
    # output: 3
    # EXPLANATION:  Place 1 rock in bag 0 and 1 rock in bag 1. The number of rocks in each bag are now [2,3,4,4]. Bags 0, 1, and 2 have full capacity. There are 3 bags at full capacity, so we return 3. It can be shown that it is not possible to have more than 3 bags at full capacity. Note that there may be other ways of placing the rocks that result in an answer of 3.
    ,
    # example 2
    [[10, 2, 2], [2, 2, 0], 100]
    # output: 3
    # EXPLANATION:  Place 8 rocks in bag 0 and 2 rocks in bag 2. The number of rocks in each bag are now [10,2,2]. Bags 0, 1, and 2 have full capacity. There are 3 bags at full capacity, so we return 3. It can be shown that it is not possible to have more than 3 bags at full capacity. Note that we did not use all of the additional rocks.
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)

##########

test()
