from L1877_MinimizeMaximumPairSuminArray import f_gold

##########
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [[3, 5, 2, 3]]
    # output: 7
    # EXPLANATION:  The elements can be paired up into pairs (3,3) and (5,2).  The maximum pair sum is max(3+3, 5+2) = max(6, 7) = 7.
    ,
    # example 2
    [[3, 5, 4, 2, 4, 6]]
    # output: 8
    # EXPLANATION:  The elements can be paired up into pairs (3,5), (4,4), and (6,2).  The maximum pair sum is max(3+5, 4+4, 6+2) = max(8, 8, 8) = 8.
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)

##########

test()
