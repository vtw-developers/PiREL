from L0942_DIStringMatch import f_gold

##########
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    ["IDID"]
    # output: [0,4,1,3,2]
    ,
    # example 2
    ["III"]
    # output: [0,1,2,3]
    ,
    # example 3
    ["DDI"]
    # output: [3,2,0,1]
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)

##########

test()
