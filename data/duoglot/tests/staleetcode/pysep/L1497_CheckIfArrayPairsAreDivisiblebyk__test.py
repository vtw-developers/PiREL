from L1497_CheckIfArrayPairsAreDivisiblebyk import f_gold

##########
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [[1, 2, 3, 4, 5, 10, 6, 7, 8, 9], 5]
    # output: true
    # EXPLANATION:  Pairs are (1,9),(2,8),(3,7),(4,6) and (5,10).
    ,
    # example 2
    [[1, 2, 3, 4, 5, 6], 7]
    # output: true
    # EXPLANATION:  Pairs are (1,6),(2,5) and(3,4).
    ,
    # example 3
    [[1, 2, 3, 4, 5, 6], 10]
    # output: false
    # EXPLANATION:  You can try all possible pairs to see that there is no way to divide arr into 3 pairs each with sum divisible by 10.
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)

##########

test()
