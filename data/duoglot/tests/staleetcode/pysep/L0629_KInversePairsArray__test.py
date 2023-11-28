from L0629_KInversePairsArray import f_gold

##########
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [3, 0]
    # output: 1
    # EXPLANATION:  Only the array [1,2,3] which consists of numbers from 1 to 3 has exactly 0 inverse pairs.
    ,
    # example 2
    [3, 1]
    # output: 2
    # EXPLANATION:  The array [1,3,2] and [2,1,3] have exactly 1 inverse pair.
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)

##########

test()
