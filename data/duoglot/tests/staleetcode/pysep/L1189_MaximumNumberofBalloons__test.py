from L1189_MaximumNumberofBalloons import f_gold

##########
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    ["nlaebolko"]
    # output: 1
    ,
    # example 2
    ["loonbalxballpoon"]
    # output: 2
    ,
    # example 3
    ["leetcode"]
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
