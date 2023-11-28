from L0361_BombEnemy import f_gold

##########
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [[["0", "E", "0", "0"], ["E", "0", "W", "E"], ["0", "E", "0", "0"]]]
    # output: 3
    ,
    # example 2
    [[["W", "W", "W"], ["0", "0", "0"], ["E", "E", "E"]]]
    # output: 1
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)

##########

test()
