from L0826_MostProfitAssigningWork import f_gold

##########
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [[2, 4, 6, 8, 10], [10, 20, 30, 40, 50], [4, 5, 6, 7]]
    # output: 100
    # EXPLANATION:  Workers are assigned jobs of difficulty [4,4,6,6] and they get a profit of [20,20,30,30] separately.
    ,
    # example 2
    [[85, 47, 57], [24, 66, 99], [40, 25, 25]]
    # output: 0
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)

##########

test()
