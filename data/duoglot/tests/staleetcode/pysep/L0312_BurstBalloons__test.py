from L0312_BurstBalloons import f_gold

##########
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [[3, 1, 5, 8]]
    # output: 167
    # EXPLANATION:  nums = [3,1,5,8] --> [3,5,8] --> [3,8] --> [8] --> [] coins =  3*1*5    +   3*5*8   +  1*3*8  + 1*8*1 = 167
    ,
    # example 2
    [[1, 5]]
    # output: 10
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)

##########

test()
