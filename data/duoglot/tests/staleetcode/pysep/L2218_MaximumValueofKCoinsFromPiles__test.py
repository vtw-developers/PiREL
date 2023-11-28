from L2218_MaximumValueofKCoinsFromPiles import f_gold

##########
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [[[1, 100, 3], [7, 8, 9]], 2]
    # output: 101
    # EXPLANATION:  The above diagram shows the different ways we can choose k coins. The maximum total we can obtain is 101.
    ,
    # example 2
    [[[100], [100], [100], [100], [100], [100], [1, 1, 1, 1, 1, 1, 700]], 7]
    # output: 706
    # EXPLANATION: The maximum total can be obtained if we choose all coins from the last pile.
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)

##########

test()
