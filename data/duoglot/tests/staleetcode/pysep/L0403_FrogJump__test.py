from L0403_FrogJump import f_gold

##########
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [[0, 1, 3, 5, 6, 8, 12, 17]]
    # output: true
    # EXPLANATION:  The frog can jump to the last stone by jumping 1 unit to the 2nd stone, then 2 units to the 3rd stone, then 2 units to the 4th stone, then 3 units to the 6th stone, 4 units to the 7th stone, and 5 units to the 8th stone.
    ,
    # example 2
    [[0, 1, 2, 3, 4, 8, 9, 11]]
    # output: false
    # EXPLANATION:  There is no way to jump to the last stone as the gap between the 5th and 6th stone is too large.
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)

##########

test()
