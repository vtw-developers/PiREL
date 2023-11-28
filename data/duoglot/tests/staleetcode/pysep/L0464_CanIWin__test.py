from L0464_CanIWin import f_gold

##########
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [10, 11]
    # output: false
    # EXPLANATION:  No matter which integer the first player choose, the first player will lose. The first player can choose an integer from 1 up to 10. If the first player choose 1, the second player can only choose integers from 2 up to 10. The second player will win by choosing 10 and get a total = 11, which is >= desiredTotal. Same with other integers chosen by the first player, the second player will always win.
    ,
    # example 2
    [10, 0]
    # output: true
    ,
    # example 3
    [10, 1]
    # output: true
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)

##########

test()
