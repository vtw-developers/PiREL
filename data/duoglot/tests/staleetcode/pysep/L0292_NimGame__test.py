from L0292_NimGame import f_gold

##########
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [4]
    # output: false
    # EXPLANATION:  These are the possible outcomes: 1. You remove 1 stone. Your friend removes 3 stones, including the last stone. Your friend wins. 2. You remove 2 stones. Your friend removes 2 stones, including the last stone. Your friend wins. 3. You remove 3 stones. Your friend removes the last stone. Your friend wins. In all outcomes, your friend wins.
    ,
    # example 2
    [1]
    # output: true
    ,
    # example 3
    [2]
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
