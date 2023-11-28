from L0875_KokoEatingBananas import f_gold

##########
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [[3, 6, 7, 11], 8]
    # output: 4
    ,
    # example 2
    [[30, 11, 23, 4, 20], 5]
    # output: 30
    ,
    # example 3
    [[30, 11, 23, 4, 20], 6]
    # output: 23
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)

##########

test()
